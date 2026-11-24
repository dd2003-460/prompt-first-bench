# N521: 公有云 CDN 缓存命中率 H_cloud 受限于全局 LRU/LFU 算法与节点间内容同步延迟，对于头部 10% 的热内容，H_cloud ≈ 95%-98%

- **status**: verified
- **level**: L5
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N169

## Claim

公有云 CDN 缓存命中率 H_cloud 受限于全局 LRU/LFU 算法与节点间内容同步延迟，对于头部 10% 的热内容，H_cloud ≈ 95%-98%；对于长尾内容，由于节点分散且容量有限，H_cloud 降至 60%-70%；加权平均 H_cloud_avg ≈ 85%-90%。

## Corrected Claim

公有云 CDN 缓存命中率 H_cloud 受限于全局 LRU/LFU 算法与节点间内容同步延迟，对于头部 10% 的热内容，H_cloud ≈ 95%-98%；对于长尾内容，由于节点分散且容量有限，H_cloud 降至 60%-70%；加权平均 H_cloud_avg ≈ 85%-90%。

## Evidence

先验知识/题面给定，逻辑校验通过
