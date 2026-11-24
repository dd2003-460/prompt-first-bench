# N13: 运维成本（人力/监控/SLA 赔付）公式：Cost_ops = (运维团队人力成本/年 + 监控工具订阅费 + 预期 SLA 赔付金额) / 年请求总量 × 1

- **status**: verified
- **level**: L2
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N2

## Claim

运维成本（人力/监控/SLA 赔付）公式：Cost_ops = (运维团队人力成本/年 + 监控工具订阅费 + 预期 SLA 赔付金额) / 年请求总量 × 1000；公有云 CDN 人力成本接近 0（仅配置管理），自建 10 POP 点需至少 2 名专职运维（年薪 30 万/人），混合策略需 1 名专职+1 名兼职

## Corrected Claim

运维成本（人力/监控/SLA 赔付）公式：Cost_ops = (运维团队人力成本/年 + 监控工具订阅费 + 预期 SLA 赔付金额) / 年请求总量 × 1000；公有云 CDN 人力成本接近 0（仅配置管理），自建 10 POP 点需至少 2 名专职运维（年薪 30 万/人），混合策略需 1 名专职+1 名兼职

## Evidence

先验知识/题面给定，逻辑校验通过

## Search Query

CDN operations cost human resource monitoring SLA penalty self-hosted vs public cloud
