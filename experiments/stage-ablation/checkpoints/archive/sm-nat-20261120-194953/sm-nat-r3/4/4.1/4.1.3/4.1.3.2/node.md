# N118: 量化冷对象对整体命中率折损的贡献：P_inval_cold * S_cold ≈ 0.01 * 0.72 = 0.0072（0.72 个百分点），其中 S_co

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N51

## Claim

量化冷对象对整体命中率折损的贡献：P_inval_cold * S_cold ≈ 0.01 * 0.72 = 0.0072（0.72 个百分点），其中 S_cold 为冷对象字节占比（1 - S_hot ≈ 0.72），此值与 N60 中基于错误 T_cold=720h 得出的 4% 折损形成对比，证明全量驻留假设下整体折损主要由均匀更新率 u 主导，而非热度分布。

## Corrected Claim

量化冷对象对整体命中率折损的贡献：P_inval_cold * S_cold ≈ 0.01 * 0.72 = 0.0072（0.72 个百分点），其中 S_cold 为冷对象字节占比（1 - S_hot ≈ 0.72），此值与 N60 中基于错误 T_cold=720h 得出的 4% 折损形成对比，证明全量驻留假设下整体折损主要由均匀更新率 u 主导，而非热度分布。

## Evidence

先验知识/题面给定，逻辑校验通过：算术运算 0.01 * 0.72 = 0.0072 正确，且符合缓存命中率折损的线性近似逻辑。
