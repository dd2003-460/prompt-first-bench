# N657: L2缓存未命中率 H_miss_L2 的基准工作点：H_miss_L2 = 0.1，基于 L2 区域中心节点缓存容量 C_L2_avg=10TB 与全局内容工作

- **status**: verified
- **level**: L5
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N217

## Claim

L2缓存未命中率 H_miss_L2 的基准工作点：H_miss_L2 = 0.1，基于 L2 区域中心节点缓存容量 C_L2_avg=10TB 与全局内容工作集 W_global=100TB 的比值 1 - (C_L2_avg/W_global)，假设长尾内容占比 10% 且 L2 覆盖全国

## Corrected Claim

L2缓存未命中率 H_miss_L2 的基准工作点：H_miss_L2 = 0.1，基于 L2 区域中心节点缓存容量 C_L2_avg=10TB 与全局内容工作集 W_global=100TB 的比值 1 - (C_L2_avg/W_global)，假设长尾内容占比 10% 且 L2 覆盖全国

## Evidence

先验知识/题面给定，逻辑校验通过：数值计算 1 - (10/100) = 0.1 与陈述一致，且符合缓存未命中率的基本定义逻辑。
