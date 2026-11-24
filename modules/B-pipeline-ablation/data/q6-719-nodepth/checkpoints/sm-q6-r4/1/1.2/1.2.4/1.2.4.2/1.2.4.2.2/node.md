# N658: L2缓存未命中率 H_miss_L2 的高性能工作点：H_miss_L2 = 0.03，通过部署大容量存储（C_L2_high=50TB/节点）并启用跨L2节点

- **status**: verified
- **level**: L5
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N217

## Claim

L2缓存未命中率 H_miss_L2 的高性能工作点：H_miss_L2 = 0.03，通过部署大容量存储（C_L2_high=50TB/节点）并启用跨L2节点的内容同步（Consistent Hashing），将全局命中率提升至 97%，对应存储成本 C_storage_L2 增加 400% 但源站带宽成本 C_bw_source 降低 70%

## Corrected Claim

L2缓存未命中率 H_miss_L2 的高性能工作点：H_miss_L2 = 0.03，通过部署大容量存储（C_L2_high=50TB/节点）并启用跨L2节点的内容同步（Consistent Hashing），将全局命中率提升至 97%，对应存储成本 C_storage_L2 增加 400% 但源站带宽成本 C_bw_source 降低 70%

## Evidence

先验知识/题面给定，逻辑校验通过：L2未命中率3%对应全局命中率97%在数学上自洽；大容量存储与一致性哈希是提升CDN L2命中率的常见工程手段，成本与带宽的权衡符合经济直觉。
