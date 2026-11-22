# N29: 在ρ=-0.3（热小冷大）场景下，LRU的字节命中率H_byte会比对象命中率H_obj高，因为命中集中在小对象上。具体修正公式：H_byte = H_obj 

- **status**: degraded
- **level**: L2
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: (root)

## Claim

在ρ=-0.3（热小冷大）场景下，LRU的字节命中率H_byte会比对象命中率H_obj高，因为命中集中在小对象上。具体修正公式：H_byte = H_obj * (E[S|Hit] / E[S])。由于E[S|Hit] < E[S]，该比值小于1但接近1，需通过Pareto截断积分计算E[S|Hit]的具体数值。

## Corrected Claim

在ρ=-0.3（热小冷大）场景下，LRU的字节命中率H_byte会比对象命中率H_obj高，因为命中集中在小对象上。具体修正公式：H_byte = H_obj * (E[S|Hit] / E[S])。由于E[S|Hit] < E[S]，该比值小于1但接近1，需通过Pareto截断积分计算E[S|Hit]的具体数值。

## Evidence

检索失败: no sources from any channel (all 5 failed)
