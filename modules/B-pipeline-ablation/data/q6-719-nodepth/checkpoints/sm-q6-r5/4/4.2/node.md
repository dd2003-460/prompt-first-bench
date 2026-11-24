# N20: 公有云CDN可行性上限：阿里云/Cloudflare单租户带宽峰值限制通常为 100Gbps-1Tbps（取决于合同等级），日均下载 2TB ≈ 平均带宽 23

- **status**: verified
- **level**: L2
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N4

## Claim

公有云CDN可行性上限：阿里云/Cloudflare单租户带宽峰值限制通常为 100Gbps-1Tbps（取决于合同等级），日均下载 2TB ≈ 平均带宽 23.1Gbps，峰值按 3x 估算为 69.3Gbps，若峰值 < 合同上限则公有云方案可行，否则需升级套餐或分流。

## Corrected Claim

公有云CDN可行性上限：阿里云/Cloudflare单租户带宽峰值限制通常为 100Gbps-1Tbps（取决于合同等级），日均下载 2TB ≈ 平均带宽 23.1Gbps，峰值按 3x 估算为 69.3Gbps，若峰值 < 合同上限则公有云方案可行，否则需升级套餐或分流。

## Evidence

先验知识/题面给定，逻辑校验通过：2TB/天换算为平均带宽约23.1Gbps，峰值3倍估算为69.3Gbps，处于公有云CDN常见合同上限（100Gbps-1Tbps）范围内，逻辑自洽且数值量级合理。

## Search Query

Alibaba Cloud CDN bandwidth cap per customer Cloudflare bandwidth limit enterprise tier
