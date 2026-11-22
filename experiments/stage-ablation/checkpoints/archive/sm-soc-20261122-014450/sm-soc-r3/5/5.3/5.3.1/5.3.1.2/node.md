# N292: 若采用 Wilson 区间而非正态近似区间，其置信区间下界 L_wilson 需通过公式 L = (p + z^2/(2n) - z*sqrt(p(1-p)/n

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N94

## Claim

若采用 Wilson 区间而非正态近似区间，其置信区间下界 L_wilson 需通过公式 L = (p + z^2/(2n) - z*sqrt(p(1-p)/n + z^2/(4n^2))) / (1 + z^2/n) 计算，以修正小样本或极端比例下的偏差。

## Corrected Claim

若采用 Wilson 区间而非正态近似区间，其置信区间下界 L_wilson 需通过公式 L = (p + z^2/(2n) - z*sqrt(p(1-p)/n + z^2/(4n^2))) / (1 + z^2/n) 计算，以修正小样本或极端比例下的偏差。

## Evidence

先验知识/题面给定，逻辑校验通过
