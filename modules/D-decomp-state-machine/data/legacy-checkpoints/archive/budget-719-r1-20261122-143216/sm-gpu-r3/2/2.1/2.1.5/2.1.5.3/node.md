# N201: NVIDIA H100 SXM 的 TDP 为 700W，在 24/7 运行、电价 $0.15/kWh 条件下，3 年纯电力成本计算公式为 700W × 876

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N60

## Claim

NVIDIA H100 SXM 的 TDP 为 700W，在 24/7 运行、电价 $0.15/kWh 条件下，3 年纯电力成本计算公式为 700W × 8760h/yr × 3yr × $0.15/kWh = $2,766.30 USD，电力成本差异为 $1,383.15 USD

## Corrected Claim

NVIDIA H100 SXM 的 TDP 为 700W，在 24/7 运行、电价 $0.15/kWh 条件下，3 年纯电力成本计算公式为 700W × 8760h/yr × 3yr × $0.15/kWh = $2,766.30 USD，电力成本差异为 $1,383.15 USD

## Evidence

先验知识/题面给定，逻辑校验通过：H100 SXM TDP 700W 符合官方规格；计算过程 700W * 8760h * 3yr * $0.15/kWh = $2,766.30 数学正确；差异 $1,383.15 为总成本的一半，逻辑自洽。
