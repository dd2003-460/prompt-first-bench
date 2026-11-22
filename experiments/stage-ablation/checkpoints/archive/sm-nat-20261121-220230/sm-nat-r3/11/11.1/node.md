# N295: 全局总数据量 S_total 的精确计算值：S_total = N * E[s_truncated] = 100,000 * 50,000 Bytes = 5,

- **status**: verified
- **level**: L4
- **source**: given
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N102

## Claim

全局总数据量 S_total 的精确计算值：S_total = N * E[s_truncated] = 100,000 * 50,000 Bytes = 5,000,000,000 Bytes (5 GB)，此处基于 N88 确认的 E[s_truncated]≈50KB 进行直接乘法运算，修正了 N102 中 5.5TB 的量级错误。

## Corrected Claim

全局总数据量 S_total 的精确计算值：S_total = N * E[s_truncated] = 100,000 * 50,000 Bytes = 5,000,000,000 Bytes (5 GB)，此处基于 N88 确认的 E[s_truncated]≈50KB 进行直接乘法运算，修正了 N102 中 5.5TB 的量级错误。

## Evidence

先验知识/题面给定，逻辑校验通过：100,000 * 50,000 Bytes = 5,000,000,000 Bytes，换算为 5 GB 正确，且符合修正量级错误的描述。
