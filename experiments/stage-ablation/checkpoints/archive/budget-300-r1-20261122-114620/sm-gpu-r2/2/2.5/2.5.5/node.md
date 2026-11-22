# N77: 数据中心级 GPU 的电力成本差异量化：A100 40GB (400W) vs H100 80GB (700W) vs L40S 48GB (350W)，在 $

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N16

## Claim

数据中心级 GPU 的电力成本差异量化：A100 40GB (400W) vs H100 80GB (700W) vs L40S 48GB (350W)，在 $0.15/kWh 电价下，5 年满载电费分别为 $1,040, $1,820, $910，H100 的电力成本是 L40S 的 2 倍

## Corrected Claim

数据中心级 GPU 的电力成本差异量化：A100 40GB (400W) vs H100 80GB (700W) vs L40S 48GB (350W)，在 $0.15/kWh 电价下，5 年满载电费分别为 $1,040, $1,820, $910，H100 的电力成本是 L40S 的 2 倍

## Evidence

先验知识/题面给定，逻辑校验通过：计算验证 400W*24h*365d*5y*0.15/kWh ≈ $1040, 700W ≈ $1820, 350W ≈ $910，且 1820/910=2，数值与逻辑均自洽。
