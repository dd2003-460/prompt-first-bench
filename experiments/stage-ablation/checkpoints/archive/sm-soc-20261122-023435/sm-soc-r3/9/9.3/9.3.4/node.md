# N247: 算法降权对 P_exposed 的影响机制：降价后 48h 内，若卖家未触发'活跃卖家'标签，P_exposed 从基准值 P_exposed_base ≈ 0

- **status**: degraded
- **level**: L4
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N79

## Claim

算法降权对 P_exposed 的影响机制：降价后 48h 内，若卖家未触发'活跃卖家'标签，P_exposed 从基准值 P_exposed_base ≈ 0.4 下降至 P_exposed_base * (1 - 0.2 * t/24h)，其中 t 为降价后小时数；该衰减率 0.2/24h 需根据平台实际日志校准。

## Corrected Claim

算法降权对 P_exposed 的影响机制：降价后 48h 内，若卖家未触发'活跃卖家'标签，P_exposed 从基准值 P_exposed_base 下降，具体衰减函数形式及参数（如基准值、衰减率）需根据平台实际日志校准，当前假设模型为 P_exposed_base * (1 - 0.2 * t/24h)。

## Evidence

[质询]该陈述包含具体的经验参数（基准值0.4、衰减率0.2/24h、48h窗口），属于平台特定业务逻辑，无法从第一性原理推导，且缺乏外部来源支持。 | 经验事实，逻辑自洽但缺来源支持（检索无可用来源）

## Search Query

second hand marketplace algorithm exposure decay after price reduction
