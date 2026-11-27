# N48: 缓存集合差异量化：ΔCache = |Cache_LFU \ Cache_LRU|，即 LFU 缓存中有但 LRU 缓存中没有的对象数量，这些对象通常是低频但较

- **status**: pending
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N11

## Claim

缓存集合差异量化：ΔCache = |Cache_LFU \ Cache_LRU|，即 LFU 缓存中有但 LRU 缓存中没有的对象数量，这些对象通常是低频但较大的对象，需计算 ΔCache 中对象的总字节流量占比。

## Corrected Claim

缓存集合差异量化：ΔCache = |Cache_LFU \ Cache_LRU|，即 LFU 缓存中有但 LRU 缓存中没有的对象数量，这些对象通常是低频但较大的对象，需计算 ΔCache 中对象的总字节流量占比。

## Evidence

父节点级核验未通过：不完备（子节点分别关注字节流量占比和对象数量占比，两者维度不同，正交性良好。但父节点明确要求计算'ΔCache 中对象的总字节流量占比'，子节点2仅关注对象数量占比，未直接覆盖父节点的核心量化指标（字节占比），且子节点1仅给出特定分布下的经验值而非通用计算方法，导致对父节点'需计算...占比'这一核心任务的覆盖不完整。）

## Search Query

cache set difference LFU LRU byte traffic contribution
