# N270: C_req_cloud 的具体计算：C_req_cloud = R_req_cloud * 30 * P_cloud_request，其中 R_req_clou

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N89

## Claim

C_req_cloud 的具体计算：C_req_cloud = R_req_cloud * 30 * P_cloud_request，其中 R_req_cloud ≈ 2.67×10^8 req/day，P_cloud_request 为公有云 CDN 单请求费用（通常极低，如 ¥0.0001-0.001/req，需查阅具体厂商 API/请求计费标准）。

## Corrected Claim

C_req_cloud 的具体计算：C_req_cloud = R_req_cloud * 30 * P_cloud_request，其中 R_req_cloud ≈ 2.67×10^8 req/day，P_cloud_request 为公有云 CDN 单请求费用（通常极低，如 ¥0.0001-0.001/req，需查阅具体厂商 API/请求计费标准）。

## Evidence

先验知识/题面给定，逻辑校验通过

## Search Query

cloudflare aliyun cdn request cost per 10000 requests
