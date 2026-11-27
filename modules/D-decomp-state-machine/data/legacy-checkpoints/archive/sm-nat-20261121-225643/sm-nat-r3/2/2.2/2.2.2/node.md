# N27: 头部对象大小影响：top 10% 对象的平均大小为 1.2MB，占缓存空间的 45%，LFU 锁定这些对象导致的空间效率损失为 0.15GB/天，但该损失被其高

- **status**: pending
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N9

## Claim

头部对象大小影响：top 10% 对象的平均大小为 1.2MB，占缓存空间的 45%，LFU 锁定这些对象导致的空间效率损失为 0.15GB/天，但该损失被其高命中率收益（+2.3%）所抵消

## Corrected Claim

头部对象大小影响：top 10% 对象的平均大小为 1.2MB，占缓存空间的 45%，LFU 锁定这些对象导致的空间效率损失为 0.15GB/天，但该损失被其高命中率收益（+2.3%）所抵消

## Evidence

父节点级核验未通过：不完备（子节点之间存在逻辑矛盾（子节点2指出45%占比计算错误，而父节点将其作为既定事实），且遗漏了父节点中关于'高命中率收益（+2.3%）'这一关键平衡因子的验证子节点。）

## Search Query

LFU space efficiency loss top objects size distribution
