# N279: 功耗对比需区分 '峰值功耗' 与 '平均运行功耗'：RTX 4090 双卡峰值 900W，但 Decode 阶段平均功耗约 600-700W；M3 Ultra 

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N124

## Claim

功耗对比需区分 '峰值功耗' 与 '平均运行功耗'：RTX 4090 双卡峰值 900W，但 Decode 阶段平均功耗约 600-700W；M3 Ultra 峰值 300W，平均约 200-250W。3 年 TCO 中电力成本差异为 (650-225)*0.15*8760 ≈ $559/年，不足以逆转性能差距

## Corrected Claim

功耗对比需区分 '峰值功耗' 与 '平均运行功耗'：RTX 4090 双卡峰值 900W，但 Decode 阶段平均功耗约 600-700W；M3 Ultra 峰值 300W，平均约 200-250W。3 年 TCO 中电力成本差异为 (650-225)*0.15*8760 ≈ $559/年，不足以逆转性能差距

## Evidence

先验知识/题面给定，逻辑校验通过：RTX 4090 TDP 450W，双卡峰值900W合理；M3 Ultra峰值300W符合Apple Silicon高端芯片功耗水平；TCO计算逻辑自洽（(650-225)W * 0.15$/kWh * 8760h ≈ $559/年），数值量级合理。
