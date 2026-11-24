# N264: 工作点1（API瓶颈-小文件场景）：若对象平均大小为1MB，受限于S3 GET 3500 req/s的前缀限制，最大有效吞吐 T_api = 3500 * 1M

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N85

## Claim

工作点1（API瓶颈-小文件场景）：若对象平均大小为1MB，受限于S3 GET 3500 req/s的前缀限制，最大有效吞吐 T_api = 3500 * 1MB = 3.5GB/s；此时API速率成为瓶颈，恢复500TB需 500,000,000MB / 3.5GB/s ≈ 143小时，远超网络带宽上限，需通过多前缀分散请求或批量API优化。

## Corrected Claim

工作点1（API瓶颈-小文件场景）：若对象平均大小为1MB，受限于S3 GET 3500 req/s的前缀限制，最大有效吞吐 T_api = 3500 * 1MB = 3.5GB/s；此时API速率成为瓶颈，恢复500TB需 500,000,000MB / 3.5GB/s ≈ 143小时，远超网络带宽上限，需通过多前缀分散请求或批量API优化。

## Evidence

先验知识/题面给定，逻辑校验通过：算术计算正确（3500 * 1MB = 3.5GB/s; 500,000,000MB / 3.5GB/s ≈ 142.857h ≈ 143h），符合S3 API限流导致吞吐受限的工程常识。
