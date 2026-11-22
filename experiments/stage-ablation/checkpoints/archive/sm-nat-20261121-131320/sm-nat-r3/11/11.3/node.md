# N158: β 的临界阈值 β_crit 的精确求解：令 ΔH_max(β) = 2%，通过二分法在 β ∈ [0.9, 1.5] 区间内求解，得到 β_crit ≈ 1.

- **status**: degraded
- **level**: L4
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N60

## Claim

β 的临界阈值 β_crit 的精确求解：令 ΔH_max(β) = 2%，通过二分法在 β ∈ [0.9, 1.5] 区间内求解，得到 β_crit ≈ 1.25；当 β < 1.25 时，LFU 提升超过 2 个百分点，值得部署；当 β > 1.25 时，LFU 提升不足 2 个百分点，LRU 更优（因 LFU 内存开销更高）。

## Corrected Claim

β 的临界阈值 β_crit 需通过求解 ΔH_max(β) = 2% 确定；在特定模型假设下，若解得 β_crit ≈ 1.25，则当 β < 1.25 时 LFU 提升显著，当 β > 1.25 时 LRU 更优。

## Evidence

[质询]该陈述包含具体的数值结果（β_crit ≈ 1.25）和特定的业务阈值（2%），属于经验事实或特定模型参数，无法从第一性原理直接推导，且缺乏来源支持。 | 经验事实，逻辑自洽但缺来源支持

## Search Query

LFU LRU cache strategy switching threshold beta critical value
