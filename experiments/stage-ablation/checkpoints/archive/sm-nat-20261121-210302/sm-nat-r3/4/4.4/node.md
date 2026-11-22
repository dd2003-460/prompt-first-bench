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

父节点级核验未通过：非正交, 不完备, 有冗余（子节点2和3存在严重冗余，它们处理的是同一类数学问题（Pareto分布截断后的方差计算），仅参数不同；子节点1与子节点2、3在逻辑上存在包含关系（计算c依赖σ），而非正交分解；父节点中提到的“字节损失”物理机制仅在子节点4中部分体现，未完全覆盖“命中率修正”与“字节损失”之间的因果链条。）

## Search Query

negative correlation size popularity LRU cache hit rate correction factor
