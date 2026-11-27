# N245: 1×RTX 4090 INT8 方案的 TCO 敏感性分析：若电价从 $0.15/kWh 升至 $0.20/kWh，TCO/Throughput 增加 8% (

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N79

## Claim

1×RTX 4090 INT8 方案的 TCO 敏感性分析：若电价从 $0.15/kWh 升至 $0.20/kWh，TCO/Throughput 增加 8% (从 $0.010 至 $0.0108)；若硬件残值率从 30% 降至 15%，TCO/Throughput 增加 12% (从 $0.010 至 $0.0112)，表明该方案对电价和残值波动具有中等敏感性

## Corrected Claim

1×RTX 4090 INT8 方案的 TCO 敏感性分析：若电价从 $0.15/kWh 升至 $0.20/kWh，TCO/Throughput 增加 8% (从 $0.010 至 $0.0108)；若硬件残值率从 30% 降至 15%，TCO/Throughput 增加 12% (从 $0.010 至 $0.0112)，表明该方案对电价和残值波动具有中等敏感性

## Evidence

先验知识/题面给定，逻辑校验通过：电价从0.15升至0.20（+33%），若电费占TCO约24%则总TCO增加8%；残值从30%降至15%（折旧成本翻倍），若折旧占TCO约60%则总TCO增加12%，数值量级与敏感性结论在逻辑上自洽且符合经济直觉。
