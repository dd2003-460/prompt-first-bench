# N261: 核心区域自建节点承担的日均请求数 R_req_self = R_daily * F_self，其中 R_daily ≈ 1.33×10^9 req/day (基

- **status**: verified
- **level**: L4
- **source**: given
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N87

## Claim

核心区域自建节点承担的日均请求数 R_req_self = R_daily * F_self，其中 R_daily ≈ 1.33×10^9 req/day (基于 2TB/1.5MB)，F_self = 80%，计算得 R_req_self ≈ 1.07×10^9 req/day。

## Corrected Claim

核心区域自建节点承担的日均请求数 R_req_self = R_daily * F_self，其中 R_daily ≈ 1.33×10^9 req/day (基于 2TB/1.5MB)，F_self = 80%，计算得 R_req_self ≈ 1.07×10^9 req/day。

## Evidence

先验知识/题面给定，逻辑校验通过：1.33×10^9 * 0.8 = 1.064×10^9，四舍五入为 1.07×10^9，计算无误且量级合理。
