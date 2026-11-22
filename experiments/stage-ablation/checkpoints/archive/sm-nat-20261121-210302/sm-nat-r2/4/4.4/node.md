# N12: 负相关 ρ≈-0.3 对 LRU 命中率的影响修正项：热门对象较小意味着 LRU 驱逐大对象时字节损失较低，命中率修正因子 f(ρ) = 1 + c*ρ，其中 

- **status**: pending
- **level**: L2
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N4

## Claim

负相关 ρ≈-0.3 对 LRU 命中率的影响修正项：热门对象较小意味着 LRU 驱逐大对象时字节损失较低，命中率修正因子 f(ρ) = 1 + c*ρ，其中 c 为耦合系数，需通过协方差 Cov(Size, Popularity) = ρ*σ_S*σ_P 量化

## Corrected Claim

负相关 ρ≈-0.3 对 LRU 命中率的影响修正项：热门对象较小意味着 LRU 驱逐大对象时字节损失较低，命中率修正因子 f(ρ) = 1 + c*ρ，其中 c 为耦合系数，需通过协方差 Cov(Size, Popularity) = ρ*σ_S*σ_P 量化

## Evidence

父节点级核验未通过：非正交, 有冗余（子节点2和3存在高度冗余，二者结构完全相同，仅参数不同（大小 vs 热度），属于同一类‘截断Pareto分布矩计算’问题；子节点1中已包含Cov的计算公式，与父节点定义重复，且子节点5中的边界条件验证依赖于前文未明确定义的Copula具体形式，逻辑链断裂。）

## Search Query

negative correlation size popularity LRU cache hit rate correction factor
