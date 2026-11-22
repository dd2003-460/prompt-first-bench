# N16: 更新率 u=1%/天 导致 LRU 有效命中率打折因子 D = 1 - u * T_LRU，其中 T_LRU 为对象在 LRU 缓存中的平均驻留时间（天），需通

- **status**: pending
- **level**: L2
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 1
- **parent_ids**: N3

## Claim

更新率 u=1%/天 导致 LRU 有效命中率打折因子 D = 1 - u * T_LRU，其中 T_LRU 为对象在 LRU 缓存中的平均驻留时间（天），需通过热度分布和容量计算 T_LRU。

## Corrected Claim

在更新率 u 较小（u * T_LRU << 1）的近似条件下，LRU 有效命中率打折因子可近似为 D ≈ 1 - u * T_LRU，其中 T_LRU 为对象在 LRU 缓存中的平均驻留时间。

## Evidence

父节点级核验未通过：非正交, 不完备, 有冗余（子节点4（H_lfu）与父节点（LRU命中率因子D）主题不一致，属于不同缓存算法的指标，导致正交性被破坏；子节点2包含大量具体数值计算细节，与子节点1的通用公式存在逻辑重叠且粒度不均；子节点3的边界条件公式引入了未定义的S_hot/S_total，且未明确与D的线性近似如何平滑过渡，存在逻辑断层。）

## Search Query

LRU cache update rate hit rate reduction factor
