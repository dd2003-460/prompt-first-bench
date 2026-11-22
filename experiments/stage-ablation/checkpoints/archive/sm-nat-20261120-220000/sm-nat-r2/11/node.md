# N64: 对象更新率1%/天导致的LRU有效命中率衰减折扣系数为 (1 - 0.01 * P_hit_updated)，其中P_hit_updated为更新对象被命中的概

- **status**: degraded
- **level**: L3
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: (root)

## Claim

对象更新率1%/天导致的LRU有效命中率衰减折扣系数为 (1 - 0.01 * P_hit_updated)，其中P_hit_updated为更新对象被命中的概率；在均匀更新假设下，折损约为1%（即乘以0.99），而非之前节点中基于极低重填充失败率的微小折损。

## Corrected Claim

对象更新率1%/天导致的LRU有效命中率衰减折扣系数为 (1 - 0.01 * P_hit_updated)，其中P_hit_updated为更新对象被命中的概率；在均匀更新假设下，折损约为1%（即乘以0.99），而非之前节点中基于极低重填充失败率的微小折损。

## Evidence

检索失败: no sources from any channel (all 5 failed)
