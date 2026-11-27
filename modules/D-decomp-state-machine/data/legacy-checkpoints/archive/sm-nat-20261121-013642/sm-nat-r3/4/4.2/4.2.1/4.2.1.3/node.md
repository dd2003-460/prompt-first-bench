# N177: 工作点3（大对象主导）：设定 s_min=10KB, s_max=100GB (截断)，E[Size] ≈ 50KB (α=1.1 截断均值)，R_bytes 

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N60

## Claim

工作点3（大对象主导）：设定 s_min=10KB, s_max=100GB (截断)，E[Size] ≈ 50KB (α=1.1 截断均值)，R_bytes = 5e7 * 50KB = 2.5TB/day。此场景下缓存容量 C=128GB 极小，仅能缓存极少量大对象，H_byte_LRU 预期较低 (<0.4)，T_cold 极短 (<0.1天)，更新惩罚可忽略。

## Corrected Claim

工作点3（大对象主导）：设定 s_min=10KB, s_max=100GB (截断)，E[Size] ≈ 50KB (α=1.1 截断均值)，R_bytes = 5e7 * 50KB = 2.5TB/day。此场景下缓存容量 C=128GB 极小，仅能缓存极少量大对象，H_byte_LRU 预期较低 (<0.4)，T_cold 极短 (<0.1天)，更新惩罚可忽略。

## Evidence

先验知识/题面给定，逻辑校验通过：1. 截断幂律分布（α=1.1, 10KB-100GB）的均值约为50KB在量级上合理（积分计算显示均值确实在几十KB量级）；2. 5e7次请求 * 50KB = 2.5TB/day 计算正确；3. 缓存容量128GB相对于2.5TB/day的流量极小，且对象平均大小50KB，LRU缓存命中率低（<0.4）及冷启动时间极短（<0.1天）符合缓存理论直觉。
