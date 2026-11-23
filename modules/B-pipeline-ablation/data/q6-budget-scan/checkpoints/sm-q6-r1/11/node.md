# N51: 单请求成本聚合公式：C_per_req = (C_total_monthly / N_requests_monthly)，其中N_requests_monthl

- **status**: degraded
- **level**: L2
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: (root)

## Claim

单请求成本聚合公式：C_per_req = (C_total_monthly / N_requests_monthly)，其中N_requests_monthly = DAU * req_per_user_per_day * 30，req_per_user_per_day为每用户日均请求数（图片+短视频平台通常为20-50次），C_total_monthly为月度总成本（基础设施+带宽+运维+安全）。

## Corrected Claim

单请求成本聚合公式：C_per_req = (C_total_monthly / N_requests_monthly)，其中N_requests_monthly = DAU * req_per_user_per_day * 30，req_per_user_per_day为每用户日均请求数（需根据具体业务场景估算），C_total_monthly为月度总成本（基础设施+带宽+运维+安全）。

## Evidence

[质询]经验参数缺乏来源支持：'req_per_user_per_day为每用户日均请求数（图片+短视频平台通常为20-50次）'属于具体的经验业务指标，参考来源均未提供该数值范围，且不同平台差异巨大，无法从第一性原理推导。 | 公式逻辑自洽（总成本/总请求数=单请求成本），来源[1]和[2]支持'单请求成本=总成本/请求数'或'全口径成本摊分'的概念，但均未覆盖'图片+短视频平台日均请求数20-50次'这一具体经验参数，故降级。

## Retrieval Sources

- {'url': 'https://www.compassingai.com/concept/cost-per-query/&rut=bdc9fdd367a973d0df50135080103774dc48c8e0932f1b8278757bde987ec858', 'type': 'ddg', 'title': 'Cost per Query Cost per Query | Compassing AI 概念库'}
- {'url': 'https://docs.pingcode.com/insights/xhhirw4p3xsphxmubgje94n6&rut=2a2f72541e6f643721fe46108e2fb27972c9e39c31f3f47cee8fca6351f69f5f', 'type': 'ddg', 'title': '单次LLM请求成本如何计算 - docs.pingcode.com'}
- {'url': 'https://learn.microsoft.com/zh-cn/azure/cost-management-billing/automate/automation-overview&rut=7cb21ea60e09a7c1cd37ffc9940dcec06ba698322fd6948313fd49e05ac4246b', 'type': 'ddg', 'title': '成本管理自动化概述 - Microsoft Cost Management'}
