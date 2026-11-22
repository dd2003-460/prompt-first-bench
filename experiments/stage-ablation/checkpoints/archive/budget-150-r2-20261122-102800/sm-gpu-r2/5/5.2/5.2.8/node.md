# N118: 年电力成本公式假设 24/7 满载运行，但实际推理负载利用率（Duty Cycle）通常为 10%-50%，需乘以实际利用率系数（如 0.3）得到真实年电力成本

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N36, N37, N38

## Claim

年电力成本公式假设 24/7 满载运行，但实际推理负载利用率（Duty Cycle）通常为 10%-50%，需乘以实际利用率系数（如 0.3）得到真实年电力成本，否则高估 2-5 倍

## Corrected Claim

年电力成本公式假设 24/7 满载运行，但实际推理负载利用率（Duty Cycle）通常为 10%-50%，需乘以实际利用率系数（如 0.3）得到真实年电力成本，否则高估 2-5 倍

## Evidence

先验知识/题面给定，逻辑校验通过：24/7满载假设与10%-50%实际利用率之间的倍数关系（1/0.5=2倍, 1/0.1=10倍，通常取中间值如0.3则高估约3.3倍，符合2-5倍量级描述）在数学和工程直觉上自洽。

## Search Query

GPU inference duty cycle typical utilization
