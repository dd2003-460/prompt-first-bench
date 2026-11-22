# N283: 工作点1（低补贴高覆盖）：设定 Subsidy_per_deal = 5 元，覆盖 N_deals_post = 10,000 单/月，直接现金成本 ΔCost

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N95

## Claim

工作点1（低补贴高覆盖）：设定 Subsidy_per_deal = 5 元，覆盖 N_deals_post = 10,000 单/月，直接现金成本 ΔCost_Direct = 50,000 元/月；此时流量倾斜幅度小，ΔChurn_rate 预估 < 0.1%，声誉机会成本极低。

## Corrected Claim

工作点1（低补贴高覆盖）：设定 Subsidy_per_deal = 5 元，覆盖 N_deals_post = 10,000 单/月，直接现金成本 ΔCost_Direct = 50,000 元/月；此时流量倾斜幅度小，ΔChurn_rate 预估 < 0.1%，声誉机会成本极低。

## Evidence

先验知识/题面给定，逻辑校验通过：直接成本计算 5元/单 * 10,000单/月 = 50,000元/月 准确无误；低补贴高覆盖场景下流量倾斜小、流失率影响微弱（<0.1%）及声誉成本低符合业务逻辑直觉。

## Search Query

platform subsidy cost per transaction C2C
