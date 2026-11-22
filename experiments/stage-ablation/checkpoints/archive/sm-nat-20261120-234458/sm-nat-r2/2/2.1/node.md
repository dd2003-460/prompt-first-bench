# N9: LFU 增益上限 = (H_LFU - H_LRU) * 100%，其中 H_LFU 假设按热度频率分配缓存空间，H_LRU 按最近访问分配；在热度 Paret

- **status**: pending
- **level**: L2
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N2

## Claim

LFU 增益上限 = (H_LFU - H_LRU) * 100%，其中 H_LFU 假设按热度频率分配缓存空间，H_LRU 按最近访问分配；在热度 Pareto(β=0.9) 下，LFU 对头部 10% 对象（占 90% 请求）的缓存保留率更高，增益上限 ≈ 5-15 个百分点 [待核验]

## Corrected Claim

LFU 增益上限 = (H_LFU - H_LRU) * 100%，其中 H_LFU 假设按热度频率分配缓存空间，H_LRU 按最近访问分配；在热度 Pareto(β=0.9) 下，LFU 对头部 10% 对象（占 90% 请求）的缓存保留率更高，增益上限 ≈ 5-15 个百分点 [待核验]

## Evidence

父节点级核验未通过：有冗余（子节点存在严重的逻辑冗余和自相矛盾。子节点1和2均得出在特定假设下命中率为100%的结论，而子节点3直接否定了前两者的前提（指出K=N时增益为0），导致前两个子节点关于‘计算模型’和‘下界’的详细推导变得无效或仅作为反例存在。此外，子节点1中关于H_LFU=100%的推导与子节点3中‘需重新定义K值’的结论在逻辑层级上重叠，且未区分‘理论上限’与‘实际增益’的区别，导致信息重复。）

## Search Query

LFU vs LRU hit rate Pareto distribution edge case
