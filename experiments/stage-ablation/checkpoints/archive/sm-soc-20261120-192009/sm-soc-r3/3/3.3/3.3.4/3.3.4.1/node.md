# N218: 工作点1（高持有成本/短周期）：设定年化持有成本率 r_holding = 5%（高值），基准周期 T0 = 30天，速度提升比例 ΔSpeed_ratio =

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N70

## Claim

工作点1（高持有成本/短周期）：设定年化持有成本率 r_holding = 5%（高值），基准周期 T0 = 30天，速度提升比例 ΔSpeed_ratio = 30%，代入 r* = (0.15) / (0.3 * (30/365)) ≈ 6.08%，此时 r_holding < r*，判定卖家受损。

## Corrected Claim

工作点1（高持有成本/短周期）：设定年化持有成本率 r_holding = 5%（高值），基准周期 T0 = 30天，速度提升比例 ΔSpeed_ratio = 30%，代入 r* = (0.15) / (0.3 * (30/365)) ≈ 6.08%，此时 r_holding < r*，判定卖家受损。

## Evidence

先验知识/题面给定，逻辑校验通过：计算过程 r* = 0.15 / (0.3 * 30/365) ≈ 6.08% 数学正确，且 5% < 6.08% 符合判定逻辑。
