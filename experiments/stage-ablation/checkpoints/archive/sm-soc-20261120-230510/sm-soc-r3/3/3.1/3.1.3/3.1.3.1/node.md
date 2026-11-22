# N184: Retention_base（基准留存率）的量化：定义为在 T_deal = T_median 且 User_Satisfaction = 0（中性）条件下的 

- **status**: degraded
- **level**: L4
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N57

## Claim

Retention_base（基准留存率）的量化：定义为在 T_deal = T_median 且 User_Satisfaction = 0（中性）条件下的 30 日用户留存率，典型值需基于平台用户生命周期数据确定（如 20%-40%）。

## Corrected Claim

Retention_base（基准留存率）定义为在 T_deal = T_median 且 User_Satisfaction = 0（中性）条件下的 30 日用户留存率，其具体典型值需基于特定平台的历史用户生命周期数据确定，而非固定为 20%-40%。

## Evidence

[质询]该陈述中的具体数值范围（20%-40%）属于经验事实，缺乏通用性，不同行业（如工具类vs社交类）差异巨大，且参考来源中未提供该特定基准值的支持。 | 逻辑自洽，但参考来源[1][3]仅解释留存率概念，未提供特定条件下的基准数值；来源[2]为无关商业网站。作为经验事实，缺乏直接来源支持，故降级。

## Search Query

e-commerce platform 30-day user retention rate baseline neutral satisfaction

## Retrieval Sources

- {'url': 'https://docs.thinkingdata.cn/ta-manual/v4.1/user_guide/analysis/retention/retention_overview.html&rut=df65eae0f74f7edff09fb8b00433b60ee9654e7056effe9d4178cd16d342d99c', 'type': 'ddg', 'title': '阶段值逻辑说明 | ThinkingData'}
- {'url': 'https://www.retentionbase.com/&rut=64e52badbe518cd2280b0d337fc8db683fcbed921c25f536260f3580ac66a9b0', 'type': 'ddg', 'title': 'AI platform that turns lost opportunities into revenue'}
- {'url': 'https://www.appier.com/zh-tw/blog/what-is-retention&rut=b1aa44d3822aff576233a8b4fc4826e4575ae34d3fcd9933bd30531158245b7c', 'type': 'ddg', 'title': '什麼是留存 (Retention) ?'}
