# N67: 工作点A的每日推理成本计算公式为 Cost_A = Power_W × 24h × Price_per_kWh，其中 Power_W 需替换为实测稳态功耗（见N

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N19, N20, N21

## Claim

工作点A的每日推理成本计算公式为 Cost_A = Power_W × 24h × Price_per_kWh，其中 Power_W 需替换为实测稳态功耗（见N30），Price_per_kWh 取 $0.15/kWh，若稳态功耗为 700W，则 Cost_A ≈ 700W × 24h × $0.15 / 1000 ≈ $2.52/天；若按峰值 1000W 计算，则 Cost_A ≈ $3.60/天

## Corrected Claim

工作点A的每日推理成本计算公式为 Cost_A = Power_W × 24h × Price_per_kWh，其中 Power_W 需替换为实测稳态功耗（见N30），Price_per_kWh 取 $0.15/kWh，若稳态功耗为 700W，则 Cost_A ≈ 700W × 24h × $0.15 / 1000 ≈ $2.52/天；若按峰值 1000W 计算，则 Cost_A ≈ $3.60/天

## Evidence

先验知识/题面给定，逻辑校验通过：700W * 24h * 0.15$/kWh / 1000 = 2.52$，1000W * 24h * 0.15$/kWh / 1000 = 3.60$，计算无误且符合物理量纲。
