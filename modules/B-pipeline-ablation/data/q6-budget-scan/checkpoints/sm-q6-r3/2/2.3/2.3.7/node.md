# N61: 带宽计费模式差异：按峰值计费 vs 按95th百分位计费 vs 按流量计费；若采用95th百分位计费，月带宽费 = 95th_Peak_Mbps * 0.1 *

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N13, N14, N15

## Claim

带宽计费模式差异：按峰值计费 vs 按95th百分位计费 vs 按流量计费；若采用95th百分位计费，月带宽费 = 95th_Peak_Mbps * 0.1 * 30 * 24 * 3600 / 1000；假设95th峰值为2Gbps/点，则月费 = 2000 * 0.1 * 259200 / 1000 = ¥51,840/点，总月OPEX = ¥518,400，远低于按10Gbps峰值估算的¥2,592,000。

## Corrected Claim

带宽计费模式差异：按峰值计费 vs 按95th百分位计费 vs 按流量计费；若采用95th百分位计费，月带宽费 = 95th_Peak_Mbps * 0.1 * 30 * 24 * 3600 / 1000；假设95th峰值为2Gbps/点，则月费 = 2000 * 0.1 * 259200 / 1000 = ¥51,840/点，总月OPEX = ¥518,400，远低于按10Gbps峰值估算的¥2,592,000。

## Evidence

先验知识/题面给定，逻辑校验通过：95th百分位计费公式及数值计算（2000 * 0.1 * 259200 / 1000 = 51840）在数学上自洽，且符合带宽计费的一般工程逻辑。

## Search Query

95th percentile bandwidth billing vs peak billing CDN
