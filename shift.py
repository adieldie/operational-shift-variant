"""Variante experimental de janela operacional.

Cada data operacional começa às 08:00 e termina às 02:00 do dia seguinte.
O limite final é exclusivo: um evento exatamente às 02:00 já está fora do
turno encerrado.
"""

from __future__ import annotations

from datetime import date, datetime, time, timedelta
from typing import Union


HORA_INICIO_TURNO = 8
HORA_FIM_TURNO = 2


def _data_base(valor: Union[str, date, datetime]) -> date:
    if isinstance(valor, datetime):
        return valor.date()
    if isinstance(valor, date):
        return valor
    if isinstance(valor, str):
        texto = valor.strip()
        for formato in ("%d-%m-%Y", "%Y-%m-%d"):
            try:
                return datetime.strptime(texto, formato).date()
            except ValueError:
                continue
    raise ValueError("Data operacional inválida. Use DD-MM-AAAA ou AAAA-MM-DD.")


def limites_data_operacional(
    valor: Union[str, date, datetime],
) -> tuple[datetime, datetime]:
    """Retorna os limites [08:00 da data, 02:00 do dia seguinte)."""

    abertura = _data_base(valor)
    inicio = datetime.combine(abertura, time(hour=HORA_INICIO_TURNO))
    fim = datetime.combine(
        abertura + timedelta(days=1),
        time(hour=HORA_FIM_TURNO),
    )
    return inicio, fim


def data_operacional_referencia(agora: datetime | None = None) -> date:
    """Retorna a data que nomeia o turno atual ou o último recém-encerrado.

    Entre 00:00 e 07:59, a referência continua sendo a data de abertura do
    turno anterior. Às 08:00 começa uma nova data operacional.
    """

    momento = (agora or datetime.now()).replace(tzinfo=None)
    if momento.hour < HORA_INICIO_TURNO:
        return momento.date() - timedelta(days=1)
    return momento.date()


def limites_turno_referencia(
    agora: datetime | None = None,
) -> tuple[datetime, datetime]:
    """Retorna o turno associado ao momento informado."""

    return limites_data_operacional(data_operacional_referencia(agora))

