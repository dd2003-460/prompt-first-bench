# N254: 自建节点利用率-成本非线性关系中的高利用率工作点（日均流量>5TB）：C_per_TB_self = C_fixed_daily / (Traffic_TB ×

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N77, N78, N79

## Claim

自建节点利用率-成本非线性关系中的高利用率工作点（日均流量>5TB）：C_per_TB_self = C_fixed_daily / (Traffic_TB × Utilization_Factor)；假设C_fixed_daily为1000元/天，Traffic_TB=5TB，Utilization_Factor=0.8（80%利用率），则C_per_TB = 1000 / (5 × 0.8) = 250元/TB，仍高于公有云CDN的0.5元/TB；但若C_fixed_daily降至100元/天（通过规模化采购和自动化运维），C_per_TB = 100 / (5 × 0.8) = 25元/TB，仍高于公有云；需进一步降低固定成本至10元/天，C_per_TB = 10 / (5 × 0.8) = 2.5元/TB，接近公有云成本。

## Corrected Claim

自建节点利用率-成本非线性关系中的高利用率工作点（日均流量>5TB）：C_per_TB_self = C_fixed_daily / (Traffic_TB × Utilization_Factor)；假设C_fixed_daily为1000元/天，Traffic_TB=5TB，Utilization_Factor=0.8（80%利用率），则C_per_TB = 1000 / (5 × 0.8) = 250元/TB，仍高于公有云CDN的0.5元/TB；但若C_fixed_daily降至100元/天（通过规模化采购和自动化运维），C_per_TB = 100 / (5 × 0.8) = 25元/TB，仍高于公有云；需进一步降低固定成本至10元/天，C_per_TB = 10 / (5 × 0.8) = 2.5元/TB，接近公有云成本。

## Evidence

先验知识/题面给定，逻辑校验通过：算术计算正确（1000/4=250, 100/4=25, 10/4=2.5），且符合自建基础设施固定成本分摊的经济直觉。

## Search Query

self-hosted CDN cost per TB high utilization break-even point
