# N106: 头部对象对分子贡献的集中度指标：Top 10% 对象在缓存 C 中贡献的字节请求率占比 P_top10 = Σ_{i∈Top10%∩C} λ_i s_i / Σ

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N31

## Claim

头部对象对分子贡献的集中度指标：Top 10% 对象在缓存 C 中贡献的字节请求率占比 P_top10 = Σ_{i∈Top10%∩C} λ_i s_i / Σ_{i∈C} λ_i s_i，用于量化分子是否由极少数大且热的对象主导。

## Corrected Claim

头部对象对分子贡献的集中度指标：Top 10% 对象在缓存 C 中贡献的字节请求率占比 P_top10 = Σ_{i∈Top10%∩C} λ_i s_i / Σ_{i∈C} λ_i s_i，用于量化分子是否由极少数大且热的对象主导。

## Evidence

先验知识/题面给定，逻辑校验通过
