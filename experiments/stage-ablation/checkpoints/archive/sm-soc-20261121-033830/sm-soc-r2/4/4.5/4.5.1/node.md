# N84: 交易量的变化量 ΔVolume = Volume_new - Volume_old，其计算依赖于需求价格弹性 η 和价格变化率 ΔP/P，即 ΔVolume/V

- **status**: degraded
- **level**: L3
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N21

## Claim

交易量的变化量 ΔVolume = Volume_new - Volume_old，其计算依赖于需求价格弹性 η 和价格变化率 ΔP/P，即 ΔVolume/Volume ≈ η * (ΔP/P)，其中 η 需基于特定二手市场实证数据估计（参考N28，弹性可能在-0.3至-0.5之间，但需具体数据验证）

## Corrected Claim

交易量的变化量 ΔVolume 与价格变化率 ΔP/P 的关系近似为 ΔVolume/Volume ≈ η * (ΔP/P)，其中 η 为需求价格弹性，需基于特定二手市场实证数据估计（具体数值范围待验证）。

## Evidence

[质询]该陈述包含具体的经验性数值范围（弹性-0.3至-0.5），属于二手市场实证数据，无法从第一性原理推导，且当前无可用外部来源支持该具体数值区间。 | 逻辑推导成立（弹性定义公式正确），但具体弹性数值范围缺乏来源支持，且检索通道失败，无法验证经验事实。

## Search Query

used goods market demand price elasticity estimation
