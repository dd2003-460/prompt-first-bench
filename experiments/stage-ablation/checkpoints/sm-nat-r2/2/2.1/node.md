# N11: LRU 缓存占用模型：稳态下缓存保留最近访问的 K 个对象，K 由总字节容量 C 和对象平均大小决定，K ≈ C / E[S]

- **status**: verified
- **level**: L2
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N2

## Claim

LRU 缓存占用模型：稳态下缓存保留最近访问的 K 个对象，K 由总字节容量 C 和对象平均大小决定，K ≈ C / E[S]

## Corrected Claim

LRU 缓存占用模型：稳态下缓存保留最近访问的 K 个对象，K 由总字节容量 C 和对象平均大小决定，K ≈ C / E[S]

## Evidence

父节点级核验通过：正交+完备+无冗余（子节点1关注理论修正模型（基于热度排序和负相关），子节点2关注基准模型的数值计算及其逻辑异常（N < K_base）。两者在逻辑上互补且无重叠：一个解释“为什么简化模型不准”，另一个展示“简化模型算出来是什么结果以及为何该结果与直觉/数据冲突”。父节点主要描述简化模型，子节点不仅覆盖了简化模型的计算（子节点2），还补充了更精确的修正模型（子节点1），从而完整解释了从简化到精确的推导过程及潜在问题。）

## Search Query

LRU cache steady state occupancy model
