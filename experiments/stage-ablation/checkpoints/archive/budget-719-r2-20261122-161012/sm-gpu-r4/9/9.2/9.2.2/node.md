# N285: RTX 5090 相对 RTX 4090 的 TDP 增加导致的年电力成本增量：假设 TDP 从 450W 增至 575W，增量 125W，在 $0.15/kW

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N126

## Claim

RTX 5090 相对 RTX 4090 的 TDP 增加导致的年电力成本增量：假设 TDP 从 450W 增至 575W，增量 125W，在 $0.15/kWh 电价下，24小时运行年增成本 = 125W * 8760h * 0.15 / 1000 ≈ $164.25

## Corrected Claim

RTX 5090 相对 RTX 4090 的 TDP 增加导致的年电力成本增量：假设 TDP 从 450W 增至 575W，增量 125W，在 $0.15/kWh 电价下，24小时运行年增成本 = 125W * 8760h * 0.15 / 1000 ≈ $164.25

## Evidence

先验知识/题面给定，逻辑校验通过：125W * 8760h = 1,095,000 Wh = 1095 kWh; 1095 kWh * $0.15/kWh = $164.25。计算无误，量纲正确。
