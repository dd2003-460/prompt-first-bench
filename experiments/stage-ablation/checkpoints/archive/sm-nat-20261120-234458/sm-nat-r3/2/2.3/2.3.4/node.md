# N42: 在 ρ_s = -0.3 且 α=1.1 的耦合分布下，头部 10% 最热门对象（频率排名 1-10000）的平均大小 S_top10% ≈ 5KB，而尾部 9

- **status**: verified
- **level**: L3
- **source**: search
- **edge_type**: quotient
- **rework_count**: 1
- **parent_ids**: N11

## Claim

在 ρ_s = -0.3 且 α=1.1 的耦合分布下，头部 10% 最热门对象（频率排名 1-10000）的平均大小 S_top10% ≈ 5KB，而尾部 90% 冷对象（频率排名 10001-100000）的平均大小 S_tail90% ≈ 15KB，导致 LRU 驱逐大冷对象造成的字节损失占比约为 (15-5)/15 ≈ 66% 的潜在可挽回字节。

## Corrected Claim

在 ρ_s = -0.3 且 α=1.1 的耦合分布下，头部热门对象平均大小显著小于尾部冷对象（例如 S_top10% < S_tail90%），导致 LRU 驱逐大冷对象造成的字节损失占比显著高于随机驱逐，具体数值需依赖特定数据集或模拟结果。

## Evidence

父节点级核验通过：正交+完备+无冗余（子节点分别处理了头部参数计算、尾部参数计算、公式逻辑修正以及边界条件假设，彼此独立且无重复。它们共同覆盖了父节点中关于数值估算、公式推导及适用前提的所有关键方面，没有遗漏核心要素，也不存在冗余。）

## Search Query

correlated frequency size distribution Pareto negative correlation cache eviction loss

## Retrieval Sources

- {'url': 'https://home.olemiss.edu/~xdang/papers/ParetoCors.pdf&rut=0bda667c58072383a39201c9e751d2a61598e37e9bac89ba8510dc8a9221cdfe', 'type': 'ddg', 'title': 'PDF Correlations in Bivariate Pareto Distributions - Ole Miss'}
- {'url': 'https://pmc.ncbi.nlm.nih.gov/articles/PMC3176775/&rut=66c869c0ec1a0b3a127def2532da2171eb67166b89a8038a7a80c7a15f960292', 'type': 'ddg', 'title': 'Modeling Fractal Structure of City-Size Distributions Using Correlation ...'}
- {'url': 'https://www.researchgate.net/publication/358736301_Correlations_in_bivariate_Pareto_distributions&rut=2fa120ea410af1083788f28693a1c2b103da3085c96e3b2919395401a637b151', 'type': 'ddg', 'title': '(PDF) Correlations in bivariate Pareto distributions - ResearchGate'}
