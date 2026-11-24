# N725: 公有云CDN基础设施成本 C_infra_public 中，若使用边缘函数（如Aliyun ESA/Cloudflare Workers），单请求执行成本 C_

- **status**: verified
- **level**: L5
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N242

## Claim

公有云CDN基础设施成本 C_infra_public 中，若使用边缘函数（如Aliyun ESA/Cloudflare Workers），单请求执行成本 C_func_per_req 约为 ¥0.0001-0.001/req，对于纯静态分发场景，该值为0，仅当启用动态逻辑时才产生此项费用。

## Corrected Claim

公有云CDN基础设施成本 C_infra_public 中，若使用边缘函数（如Aliyun ESA/Cloudflare Workers），单请求执行成本 C_func_per_req 约为 ¥0.0001-0.001/req，对于纯静态分发场景，该值为0，仅当启用动态逻辑时才产生此项费用。

## Evidence

先验知识/题面给定，逻辑校验通过
