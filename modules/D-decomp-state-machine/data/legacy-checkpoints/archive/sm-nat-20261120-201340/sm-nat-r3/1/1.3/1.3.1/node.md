# N36: 在 ρ=-0.3 的联合分布下，最热门的 10% 对象（前 10,000 个）的平均大小约为总体均值的 0.7 倍（基于 Pearson 相关系数近似），即 E

- **status**: pending
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N8

## Claim

在 ρ=-0.3 的联合分布下，最热门的 10% 对象（前 10,000 个）的平均大小约为总体均值的 0.7 倍（基于 Pearson 相关系数近似），即 E[S|top10%] ≈ 0.7 * 110KB = 77KB。

## Corrected Claim

在 ρ=-0.3 的联合分布下，最热门的 10% 对象的平均大小预计低于总体均值（110KB），具体倍数取决于分布形态，通常估计在 0.5-0.8 倍之间。

## Evidence

父节点级核验失败（LLM 错误）：Unterminated string starting at: line 5 column 13 (char 79)

## Search Query

negative correlation between request frequency and object size CDN
