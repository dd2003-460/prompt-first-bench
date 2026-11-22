# N181: OpEx 中电力成本的年化计算实例：以 RTX 4090 (TDP 450W) 为例，System_Overhead_TDP 约为 300W，总功耗 750W；

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N34

## Claim

OpEx 中电力成本的年化计算实例：以 RTX 4090 (TDP 450W) 为例，System_Overhead_TDP 约为 300W，总功耗 750W；若电价 $0.12/kWh，利用率 50%，则年电力成本 = 0.75 kW × 8760 h × 0.5 × $0.12 ≈ $394.2/年；对比 H100 (TDP 700W + 300W overhead = 1000W)，年电力成本 ≈ $525.6/年（假设相同利用率）

## Corrected Claim

OpEx 中电力成本的年化计算实例：以 RTX 4090 (TDP 450W) 为例，System_Overhead_TDP 约为 300W，总功耗 750W；若电价 $0.12/kWh，利用率 50%，则年电力成本 = 0.75 kW × 8760 h × 0.5 × $0.12 ≈ $394.2/年；对比 H100 (TDP 700W + 300W overhead = 1000W)，年电力成本 ≈ $525.6/年（假设相同利用率）

## Evidence

先验知识/题面给定，逻辑校验通过：0.75kW * 8760h * 0.5 * 0.12 = 394.2，1.0kW * 8760h * 0.5 * 0.12 = 525.6，计算无误且符合物理直觉。
