# N215: C_search_pre 的具体数值估算：C_search_pre = T_pre * C_time，其中 T_pre 为高挂价现象出现前买家平均单次有效搜索耗

- **status**: verified
- **level**: L4
- **source**: given
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N83

## Claim

C_search_pre 的具体数值估算：C_search_pre = T_pre * C_time，其中 T_pre 为高挂价现象出现前买家平均单次有效搜索耗时（基于历史数据假设 T_pre = 17 min，参考 N57），C_time 为时间机会成本（假设 10 元/小时），故 C_search_pre = (17/60) * 10 ≈ 2.83 元。

## Corrected Claim

C_search_pre 的具体数值估算：C_search_pre = T_pre * C_time，其中 T_pre 为高挂价现象出现前买家平均单次有效搜索耗时（基于历史数据假设 T_pre = 17 min，参考 N57），C_time 为时间机会成本（假设 10 元/小时），故 C_search_pre = (17/60) * 10 ≈ 2.83 元。

## Evidence

先验知识/题面给定，逻辑校验通过：计算过程 (17/60)*10 ≈ 2.83 数学正确，量纲（元）合理，符合给定假设。
