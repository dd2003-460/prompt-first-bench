# N68: 对于 Pareto(α=1.1, s_min=1KB) 分布，累计字节占比 B(x) = 1 - (s_min/x)^0.1；求解 B(x) = 0.99 得 

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N25

## Claim

对于 Pareto(α=1.1, s_min=1KB) 分布，累计字节占比 B(x) = 1 - (s_min/x)^0.1；求解 B(x) = 0.99 得 x ≈ 1.26×10^12 bytes (1.26TB)，远大于单对象最大合理尺寸，表明 99% 的字节集中在极少数的超大对象中；k_max 并非由总容量决定，而是由‘能容纳多少个头部超大对象’决定，具体 k_max ≈ N * P(S > S_threshold)，其中 S_threshold 是使得前 k_max 个对象总大小等于 C 的阈值。

## Corrected Claim

对于 Pareto(α=1.1, s_min=1KB) 分布，累计字节占比 B(x) = 1 - (s_min/x)^0.1；求解 B(x) = 0.99 得 x ≈ 1.26×10^12 bytes (1.26TB)，远大于单对象最大合理尺寸，表明 99% 的字节集中在极少数的超大对象中；k_max 并非由总容量决定，而是由‘能容纳多少个头部超大对象’决定，具体 k_max ≈ N * P(S > S_threshold)，其中 S_threshold 是使得前 k_max 个对象总大小等于 C 的阈值。

## Evidence

先验知识/题面给定，逻辑校验通过：Pareto分布尾部积分公式推导正确，数值量级（1.26TB）符合α=1.1时的长尾特性，k_max定义逻辑自洽。
