# N176: 工作点2（混合大小）：设定 s_min=1KB, s_max=10GB (截断)，E[Size] ≈ 10KB (α=1.1 截断均值，受 s_max 限制)，

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N60

## Claim

工作点2（混合大小）：设定 s_min=1KB, s_max=10GB (截断)，E[Size] ≈ 10KB (α=1.1 截断均值，受 s_max 限制)，R_bytes = 5e7 * 10KB = 500GB/day。此场景下缓存容量 C=128GB 仅覆盖 Top-K 大对象，H_byte_LRU 预期中等 (0.6-0.7)，与 N58/N59 的 T_cold 计算基准一致。

## Corrected Claim

工作点2（混合大小）：设定 s_min=1KB, s_max=10GB (截断)，E[Size] ≈ 10KB (α=1.1 截断均值，受 s_max 限制)，R_bytes = 5e7 * 10KB = 500GB/day。此场景下缓存容量 C=128GB 仅覆盖 Top-K 大对象，H_byte_LRU 预期中等 (0.6-0.7)，与 N58/N59 的 T_cold 计算基准一致。

## Evidence

先验知识/题面给定，逻辑校验通过：算术计算 5e7 * 10KB = 500GB 正确；Zipf 分布截断均值及 LRU 命中率量级符合缓存理论常识。
