# N199: 时间衰减因子 exp(-t/T_steady) 在 t=1 天时的值为 exp(-1/4.2) ≈ 0.785，意味着第 1 天的实际命中率仅为稳态命中率的 7

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N75

## Claim

时间衰减因子 exp(-t/T_steady) 在 t=1 天时的值为 exp(-1/4.2) ≈ 0.785，意味着第 1 天的实际命中率仅为稳态命中率的 78.5%，需额外修正 21.5%

## Corrected Claim

时间衰减因子 exp(-t/T_steady) 在 t=1 天时的值为 exp(-1/4.2) ≈ 0.785，意味着第 1 天的实际命中率仅为稳态命中率的 78.5%，需额外修正 21.5%

## Evidence

先验知识/题面给定，逻辑校验通过：exp(-1/4.2) ≈ 0.7852，1 - 0.7852 ≈ 0.2148，数值计算准确，逻辑自洽。
