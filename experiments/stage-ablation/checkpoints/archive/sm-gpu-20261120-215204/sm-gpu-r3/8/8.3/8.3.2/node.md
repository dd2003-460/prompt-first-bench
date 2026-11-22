# N385: A100 80GB SXM4 3年TCO构成：硬件Capex $18,000 (二手/租赁折算) + 电力成本 (400W TDP * 0.8负载系数 * 87

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N145

## Claim

A100 80GB SXM4 3年TCO构成：硬件Capex $18,000 (二手/租赁折算) + 电力成本 (400W TDP * 0.8负载系数 * 8760h/年 * 3年 * $0.15/kWh) ≈ $1,300，总TCO ≈ $19,300；N145中$18,500接近此估算，但需确认硬件采购渠道（新品vs二手）对Capex的影响。

## Corrected Claim

A100 80GB SXM4 3年TCO构成：硬件Capex $18,000 (二手/租赁折算) + 电力成本 (400W TDP * 0.8负载系数 * 8760h/年 * 3年 * $0.15/kWh) ≈ $1,300，总TCO ≈ $19,300；N145中$18,500接近此估算，但需确认硬件采购渠道（新品vs二手）对Capex的影响。

## Evidence

先验知识/题面给定，逻辑校验通过：电力成本计算 400W * 0.8 * 8760h * 3 * $0.15/kWh ≈ $1,300 准确，硬件Capex $18,000 符合A100二手/租赁折算的市场量级，总TCO加和逻辑自洽。

## Search Query

A100 80GB SXM4 3 year total cost of ownership electricity cost calculation
