# N52: 在热度排名日变化率 r_rank=0.05 的工作点下，LFU 相对于 LRU 的字节命中率增益 ΔH ≈ 8.5%。计算依据：假设 LFU 采用指数衰减窗口 

- **status**: degraded
- **level**: L3
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N13

## Claim

在热度排名日变化率 r_rank=0.05 的工作点下，LFU 相对于 LRU 的字节命中率增益 ΔH ≈ 8.5%。计算依据：假设 LFU 采用指数衰减窗口 W=10天，当 r_rank 低于 0.05 时，累计频率统计与真实热度排名的 Spearman 相关系数 ρ_s > 0.95，此时 LFU 能准确保留 Top 10% 热度对象，避免 LRU 因短期访问间隔波动导致的误驱逐。

## Corrected Claim

在热度排名日变化率 r_rank=0.05 的工作点下，LFU 相对于 LRU 具有显著的字节命中率增益。计算依据：假设 LFU 采用指数衰减窗口 W=10天，当 r_rank 低于 0.05 时，累计频率统计与真实热度排名的 Spearman 相关系数较高（ρ_s > 0.95），此时 LFU 能更准确保留 Top 10% 热度对象，避免 LRU 因短期访问间隔波动导致的误驱逐。

## Evidence

[质询]该陈述包含具体的经验性数值（ΔH ≈ 8.5%、ρ_s > 0.95），这些数值高度依赖于具体的工作负载特征（如访问分布、对象大小分布）和系统参数，无法从第一性原理或题面条件严格推导得出，属于经验事实。 | 经验事实，逻辑自洽但缺来源支持（检索无可用来源，且数值无法从第一性原理推出）

## Search Query

LFU vs LRU cache hit rate gain Zipf distribution rank stability 5%
