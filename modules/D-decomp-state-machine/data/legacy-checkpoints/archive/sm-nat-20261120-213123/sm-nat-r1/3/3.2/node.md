# N15: 在 ρ=-0.3 的负相关下，LRU 命中率需乘以修正因子 K(ρ) ≈ 1 + ρ * (Var(H)/E[H]^2)，其中 Var(H)/E[H]^2 为热

- **status**: degraded
- **level**: L2
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N3

## Claim

在 ρ=-0.3 的负相关下，LRU 命中率需乘以修正因子 K(ρ) ≈ 1 + ρ * (Var(H)/E[H]^2)，其中 Var(H)/E[H]^2 为热度分布的变异系数平方，量化相关性对命中率的影响。

## Corrected Claim

在 ρ=-0.3 的负相关下，LRU 命中率会受到请求间相关性及热度分布离散程度的影响，但具体的修正因子 K(ρ) 需依据特定的缓存模型或实验数据确定，不存在通用的简单解析公式 K(ρ) ≈ 1 + ρ * (Var(H)/E[H]^2)。

## Evidence

[质询]该公式 K(ρ) ≈ 1 + ρ * (Var(H)/E[H]^2) 缺乏公认的学术或工程标准支持，属于高度可疑的特定模型假设或杜撰公式；LRU命中率与请求间相关性（ρ）及热度分布变异系数（CV²）之间通常不存在如此简单线性的解析关系，且负相关（ρ=-0.3）对LRU的影响机制复杂，不能仅通过此简单因子修正。 | 经验事实/特定模型参数，逻辑量纲自洽（无量纲修正因子），但无来源支持且非第一性原理可推导，检索无可用来源，故降级。

## Search Query

cache hit rate correction factor negative correlation size popularity
