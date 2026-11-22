# N11: LFU 最大提升幅度上界：ΔH = H_LFU_max - H_LRU ≈ [Σ_{i∈C_LFU} r_i s_i / Total - Σ_{i∈C_LRU}

- **status**: degraded
- **level**: L2
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N1, N2, N3

## Claim

LFU 最大提升幅度上界：ΔH = H_LFU_max - H_LRU ≈ [Σ_{i∈C_LFU} r_i s_i / Total - Σ_{i∈C_LRU} r_i s_i / Total]，其中 C_LFU 按频率排序，C_LRU 按时间排序；在 β=0.9 稳定热度下，LFU 可避免 LRU 的 5-8% 命中率损失，量化为 ΔH_max ≈ 0.05-0.08 百分点。

## Corrected Claim

在β=0.9稳定热度分布下，LFU通常能避免LRU因时间局部性失效导致的命中率损失，具体提升幅度取决于负载特征，典型场景下可达数个百分比点。

## Evidence

[质询]数值量级与具体百分比（5-8%）缺乏普适性，高度依赖工作负载特征（如Zipf指数、缓存大小），将其作为通用上界陈述存在以偏概全的风险；且公式中ΔH定义为命中率差值，单位应为绝对值（如0.05-0.08）而非'百分点'（通常指相对变化或需明确语境），存在口径模糊。 | source=knowledge，逻辑自洽（LFU在稳定热度下优于LRU符合缓存理论直觉，公式结构合理），但具体数值5-8%为经验估计，无外部来源直接支持，且缺乏特定负载条件限定，故降级为定性表述。

## Search Query

LFU vs LRU hit rate improvement Pareto stable workload maximum gain percentage
