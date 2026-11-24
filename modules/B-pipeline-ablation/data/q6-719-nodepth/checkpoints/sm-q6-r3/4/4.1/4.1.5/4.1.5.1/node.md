# N249: 峰值带宽安全余量系数 Safety_Factor_BW 的确定依据：Safety_Factor_BW = 1 / (1 - P99_Traffic_Spike_

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N81

## Claim

峰值带宽安全余量系数 Safety_Factor_BW 的确定依据：Safety_Factor_BW = 1 / (1 - P99_Traffic_Spike_Probability)，其中 P99_Traffic_Spike_Probability 为 P99 流量突发超出峰值预测的概率（典型 10%-20%）；若取 15%，则 Safety_Factor_BW = 1 / (1 - 0.15) ≈ 1.18，与题面 1.2 接近，用于计算所需合同带宽 83.16Gbps。

## Corrected Claim

峰值带宽安全余量系数 Safety_Factor_BW 的确定依据：Safety_Factor_BW = 1 / (1 - P99_Traffic_Spike_Probability)，其中 P99_Traffic_Spike_Probability 为 P99 流量突发超出峰值预测的概率（典型 10%-20%）；若取 15%，则 Safety_Factor_BW = 1 / (1 - 0.15) ≈ 1.18，与题面 1.2 接近，用于计算所需合同带宽 83.16Gbps。

## Evidence

先验知识/题面给定，逻辑校验通过：公式 1/(1-0.15) ≈ 1.176 四舍五入为 1.2 符合工程近似惯例，且 83.16Gbps 与 1.2 系数在量级上自洽（隐含基础带宽约 69.3Gbps，属合理范围）。

## Search Query

CDN bandwidth safety margin factor peak traffic prediction error
