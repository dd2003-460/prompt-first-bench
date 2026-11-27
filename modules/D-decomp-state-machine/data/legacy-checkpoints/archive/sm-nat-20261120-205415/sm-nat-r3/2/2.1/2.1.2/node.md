# N41: 分子（缓存内请求字节数）的解析近似为 Num = Q_total * P(Hit_LRU)，其中 Q_total 为总请求字节数；在 Pareto(β=0.9)

- **status**: pending
- **level**: L3
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N10

## Claim

分子（缓存内请求字节数）的解析近似为 Num = Q_total * P(Hit_LRU)，其中 Q_total 为总请求字节数；在 Pareto(β=0.9) 热度下，前 K 个最热门对象的请求概率占比 P_topK = 1 - (K/N)^(1-β)（若按 Zipf 排名近似）。

## Corrected Claim

分子（缓存内请求字节数）的解析近似为 Num = Q_total * P(Hit_LRU)，其中 Q_total 为总请求字节数；在 Pareto(β=0.9) 热度下，前 K 个最热门对象的请求概率占比 P_topK = 1 - (K/N)^(1-β)（若按 Zipf 排名近似）。

## Evidence

父节点级核验未通过：非正交, 有冗余（子节点1和子节点4存在逻辑冲突与冗余：子节点1声称公式 $1-(K/N)^{1-\beta}$ 不可用，而子节点4直接使用该近似逻辑（或基于其修正）得出具体数值，且两者都在讨论 Zipf 分布下的头部占比计算，属于同一主题的不同实例，未完全正交。此外，子节点2和子节点3分别计算了公式中的分母（K）和分子（Total_Bytes），虽然正交，但子节点1和4均涉及 $P_{topK}$ 的计算细节，存在重叠。）

## Search Query

Zipf law cumulative probability top k items
