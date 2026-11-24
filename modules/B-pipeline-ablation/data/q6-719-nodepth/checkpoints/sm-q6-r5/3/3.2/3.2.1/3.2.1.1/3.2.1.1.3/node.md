# N649: 公有云缓存容量与命中率的 Trade-off 工作点 2（中容量中命中率）：假设公有云全局缓存池容量 C_pool ≈ 10TB（匹配日均 2TB 下载量的热数

- **status**: verified
- **level**: L5
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N217

## Claim

公有云缓存容量与命中率的 Trade-off 工作点 2（中容量中命中率）：假设公有云全局缓存池容量 C_pool ≈ 10TB（匹配日均 2TB 下载量的热数据子集），覆盖 Top 80% 热对象，此时 H_cloud ≈ 0.90，是成本与性能平衡的最优工作点，也是 N217 中 0.90 数值的来源。

## Corrected Claim

公有云缓存容量与命中率的 Trade-off 工作点 2（中容量中命中率）：假设公有云全局缓存池容量 C_pool ≈ 10TB（匹配日均 2TB 下载量的热数据子集），覆盖 Top 80% 热对象，此时 H_cloud ≈ 0.90，是成本与性能平衡的最优工作点，也是 N217 中 0.90 数值的来源。

## Evidence

先验知识/题面给定，逻辑校验通过
