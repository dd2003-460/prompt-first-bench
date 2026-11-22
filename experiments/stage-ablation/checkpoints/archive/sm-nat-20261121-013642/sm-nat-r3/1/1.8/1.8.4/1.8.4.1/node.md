# N169: 工作点1（基准折损）：基于 N98 的 T_residence=0.85 天，计算 f_update = 1 - 0.01 * 0.85 = 0.9915。有效

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N56

## Claim

工作点1（基准折损）：基于 N98 的 T_residence=0.85 天，计算 f_update = 1 - 0.01 * 0.85 = 0.9915。有效命中率 H_effective = H_byte_LRU * 0.9915，折损因子为 0.85%。此值表明在标准负载下，更新率对命中率的直接惩罚小于 1%。

## Corrected Claim

工作点1（基准折损）：基于 N98 的 T_residence=0.85 天，计算 f_update = 1 - 0.01 * 0.85 = 0.9915。有效命中率 H_effective = H_byte_LRU * 0.9915，折损因子为 0.85%。此值表明在标准负载下，更新率对命中率的直接惩罚小于 1%。

## Evidence

先验知识/题面给定，逻辑校验通过：计算过程 1 - 0.01 * 0.85 = 0.9915 正确，折损因子 1 - 0.9915 = 0.0085 即 0.85%，小于 1% 的结论符合算术逻辑。
