# N140: λ_search 的操作化定义与数据源：λ_search = N_search_requests / T_online，其中 N_search_requests

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N40

## Claim

λ_search 的操作化定义与数据源：λ_search = N_search_requests / T_online，其中 N_search_requests 为用户在 T_online 时间窗口内点击搜索框或输入关键词的次数，T_online 为客户端心跳包统计的活跃时长，需排除后台挂起时间。

## Corrected Claim

λ_search 的操作化定义与数据源：λ_search = N_search_requests / T_online，其中 N_search_requests 为用户在 T_online 时间窗口内点击搜索框或输入关键词的次数，T_online 为客户端心跳包统计的活跃时长，需排除后台挂起时间。

## Evidence

先验知识/题面给定，逻辑校验通过
