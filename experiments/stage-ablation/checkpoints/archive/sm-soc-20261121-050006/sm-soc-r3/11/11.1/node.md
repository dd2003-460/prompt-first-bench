# N351: 信息获取成本 C_info 的量化分解为 C_info = T_search * W_buyer + C_cognitive，其中 T_search 为单次有效

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N114

## Claim

信息获取成本 C_info 的量化分解为 C_info = T_search * W_buyer + C_cognitive，其中 T_search 为单次有效比价平均耗时（基于日志统计，如 3-5 分钟），W_buyer 为买家时间机会成本（如 50 元/小时），C_cognitive 为处理价格分布的认知负荷（可通过 A/B 测试中决策延迟增量量化，如 10-20 元等价效用）。

## Corrected Claim

信息获取成本 C_info 的量化分解为 C_info = T_search * W_buyer + C_cognitive，其中 T_search 为单次有效比价平均耗时（基于日志统计，如 3-5 分钟），W_buyer 为买家时间机会成本（如 50 元/小时），C_cognitive 为处理价格分布的认知负荷（可通过 A/B 测试中决策延迟增量量化，如 10-20 元等价效用）。

## Evidence

先验知识/题面给定，逻辑校验通过
