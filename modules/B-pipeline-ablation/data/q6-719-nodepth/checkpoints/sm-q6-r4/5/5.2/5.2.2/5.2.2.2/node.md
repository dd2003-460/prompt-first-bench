# N279: 公有云策略总月度成本 C_total_cloud 的汇总：若采用阿里云流量计费，C_total_cloud ≈ C_bw_cloud (¥12,000) + C

- **status**: degraded
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N92

## Claim

公有云策略总月度成本 C_total_cloud 的汇总：若采用阿里云流量计费，C_total_cloud ≈ C_bw_cloud (¥12,000) + C_req_cloud (¥0) + C_opex_cloud (监控/管理 ¥5,000) ≈ ¥17,000/月；若采用 Cloudflare，C_total_cloud ≈ C_bw_cloud (按 $0.04/GB ≈ ¥0.28/GB, 60TB -> ¥50,000) + C_req_cloud (¥1,447,200) ≈ ¥1,497,200/月，差异巨大，需根据厂商定价模型重新评估。

## Corrected Claim

公有云策略总月度成本 C_total_cloud 的汇总：若采用阿里云流量计费，C_total_cloud ≈ C_bw_cloud (¥12,000) + C_req_cloud (需根据实际请求量估算) + C_opex_cloud (监控/管理 ¥5,000)；若采用 Cloudflare，C_total_cloud ≈ C_bw_cloud (按 $0.04/GB ≈ ¥0.28/GB, 60TB -> ¥50,000) + C_req_cloud (需根据实际请求量估算)，具体数值需根据厂商最新定价模型及实际业务量重新评估。

## Evidence

[质询]Cloudflare 的请求费用（C_req_cloud）高达 ¥1,447,200/月，远超带宽费用，且阿里云请求费用为 0 的假设缺乏依据（通常 API 调用或对象存储请求均有计费项），具体数值属于经验事实且缺乏来源支持。 | 经验事实，逻辑自洽但缺来源支持
