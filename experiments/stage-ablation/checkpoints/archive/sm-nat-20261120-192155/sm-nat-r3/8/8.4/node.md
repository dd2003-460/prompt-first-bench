# N50: 对于Pareto分布热度 r_i ∝ i^{-0.9}，头部对象（i=1..10）的访问频率占比约为 90%，其平均驻留时间 T_res 约为 1/(10 * 

- **status**: pending
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N19

## Claim

对于Pareto分布热度 r_i ∝ i^{-0.9}，头部对象（i=1..10）的访问频率占比约为 90%，其平均驻留时间 T_res 约为 1/(10 * r_1) 秒（假设总请求率 R_total=5e7/day），即 T_res ≈ 172800 / (10 * 0.9 * 5e7/100000) ≈ 0.0038 秒，远小于更新间隔 T_upd=1天，因此热门对象几乎每次访问前都未更新，折扣主要来源于中尾部对象。

## Corrected Claim

对于Pareto分布热度 r_i ∝ i^{-0.9}，头部对象（i=1..10）的访问频率占比约为10-20%，其平均驻留时间需根据具体缓存策略和请求率重新计算，不能简单用1/(10*r_1)估算。

## Evidence

父节点级核验失败（LLM 错误）：Unterminated string starting at: line 10 column 5 (char 802)

## Search Query

Pareto distribution access frequency residence time calculation
