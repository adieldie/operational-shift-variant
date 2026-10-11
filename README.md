# Operational shift — experimental variant

**Estágio: experimental / em teste. Demonstração parcial sanitizada, não pronta para produção.**

Selected-source snapshot from a duplicate/revision branch of an operational dashboard. Its shift module is identical to the related operational-shift-demo source. This is explicitly a variant, not a second independently implemented product.

## Purpose
Compute a shift window across midnight and derive an operational reference date. Operational branding is removed and the 08:00–02:00 schedule is fictional. The rule itself is unchanged. No dashboard, database, robot, credentials, logs or production integration is included.

## Inspect and use
Python 3.10+, standard library only:

```python
from shift import limites_data_operacional
print(limites_data_operacional("2030-01-15"))
```

## Stage
Experimental selected module. No fixes or feature development were performed. No runtime or end-to-end tests were run for this separate variant. Date-times are local and naive; this is not a timezone conversion service. The full duplicate dashboard remains outside this snapshot.

No license grant is assumed. Original private repositories and history remain unchanged.
