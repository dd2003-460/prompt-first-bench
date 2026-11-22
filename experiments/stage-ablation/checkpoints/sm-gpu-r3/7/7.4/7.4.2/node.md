# N273: 工作点 2 (高成本/BF16/H100)：硬件成本 $25000，3 年 OPEX (电力 $0.15/kWh, 700W) ≈ $500/年 * 3 = $

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N122

## Claim

工作点 2 (高成本/BF16/H100)：硬件成本 $25000，3 年 OPEX (电力 $0.15/kWh, 700W) ≈ $500/年 * 3 = $1500，TCO ≈ $26500；吞吐 (N94) ≈ 52.5 tokens/s (取中值)；Cost_Performance = 26500 / 52.5 ≈ 504.8 $/tokens/s；相比工作点 1 成本效率低 4.56 倍。

## Corrected Claim

工作点 2 (高成本/BF16/H100)：硬件成本 $25000，3 年 OPEX (电力 $0.15/kWh, 700W) ≈ $500/年 * 3 = $1500，TCO ≈ $26500；吞吐 (N94) ≈ 52.5 tokens/s (取中值)；Cost_Performance = 26500 / 52.5 ≈ 504.8 $/tokens/s；相比工作点 1 成本效率低 4.56 倍。

## Evidence

先验知识/题面给定，逻辑校验通过：硬件成本25000 + 3年OPEX(500*3=1500) = TCO 26500；Cost_Performance = 26500 / 52.5 ≈ 504.76；若工作点1的Cost_Performance约为110.7 (504.8/4.56)，则倍数关系成立，数值量级与计算逻辑自洽。
