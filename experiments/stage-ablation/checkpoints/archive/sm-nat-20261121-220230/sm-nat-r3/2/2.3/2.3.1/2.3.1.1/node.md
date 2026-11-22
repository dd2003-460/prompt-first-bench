# N152: LFU 增益 ΔH 随热度排名日变化率 r_rank 变化的非线性边界：当 r_rank < 0.1 时，ΔH ≈ 8.5%；当 r_rank > 0.3 时，

- **status**: degraded
- **level**: L4
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 1
- **parent_ids**: N52

## Claim

LFU 增益 ΔH 随热度排名日变化率 r_rank 变化的非线性边界：当 r_rank < 0.1 时，ΔH ≈ 8.5%；当 r_rank > 0.3 时，ΔH < 1%。在 r_rank=0.05 的工作点，Spearman 相关系数 ρ_s 的解析近似为 ρ_s ≈ 1 - 0.5 * r_rank * (W/Δt)，代入 W=10天, Δt=1小时 得 ρ_s ≈ 0.997，验证了 N52 中 ρ_s > 0.95 的假设。

## Corrected Claim

在特定负载模型下，LFU 增益 ΔH 随热度排名日变化率 r_rank 变化呈现非线性边界：当 r_rank < 0.1 时，ΔH 约为 8.5%；当 r_rank > 0.3 时，ΔH 小于 1%。在 r_rank=0.05 的工作点，基于特定解析近似模型，Spearman 相关系数 ρ_s 约为 0.997，满足 ρ_s > 0.95 的假设。

## Evidence

[质询]该陈述包含具体的经验性数值（如 ΔH ≈ 8.5%、ρ_s ≈ 0.997）和特定的解析近似公式，这些并非 LFU 算法或统计学的通用第一性原理推论，而是依赖于特定数据集、负载模型或实验环境的经验事实。缺乏通用理论支持，且具体数值量级（如 8.5% 的增益）在无特定上下文时无法从基本逻辑推导得出。 | 经验事实，逻辑自洽但缺来源支持；具体数值和公式属于特定场景下的经验参数，非通用理论结论。

## Search Query

LFU vs LRU gain sensitivity to workload volatility rank change rate
