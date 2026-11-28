# N646: 电价敏感上限：当电价 Price_per_kWh 升至 $0.50/kWh（如部分商业高峰电价）时，单日本地能耗成本上限 Cost_Max = (1000W *

- **status**: verified
- **level**: L5
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N237

## Claim

电价敏感上限：当电价 Price_per_kWh 升至 $0.50/kWh（如部分商业高峰电价）时，单日本地能耗成本上限 Cost_Max = (1000W * 24h / 1000) * $0.50 * 0.8 = $9.60，此时本地推理成本显著上升，需重新评估云端 API 替代方案的性价比拐点。

## Corrected Claim

电价敏感上限：当电价 Price_per_kWh 升至 $0.50/kWh（如部分商业高峰电价）时，单日本地能耗成本上限 Cost_Max = (1000W * 24h / 1000) * $0.50 * 0.8 = $9.60，此时本地推理成本显著上升，需重新评估云端 API 替代方案的性价比拐点。

## Evidence

先验知识/题面给定，逻辑校验通过：计算过程 (1000W * 24h / 1000) * $0.50 * 0.8 = 24 * 0.5 * 0.8 = $9.60 准确无误，符合物理与经济直觉。
