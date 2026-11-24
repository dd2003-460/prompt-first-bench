# N735: 低带宽配置下的硬件利用率 Utilization_Hardware = Actual_Traffic / Reserved_Bandwidth，若 Actual

- **status**: verified
- **level**: L5
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N252

## Claim

低带宽配置下的硬件利用率 Utilization_Hardware = Actual_Traffic / Reserved_Bandwidth，若 Actual_Traffic 平均为 10 Mbps，Reserved 为 16.67 Mbps，则 Utilization ≈ 60%，剩余 40% 带宽为闲置资源，需评估是否可复用或降级

## Corrected Claim

低带宽配置下的硬件利用率 Utilization_Hardware = Actual_Traffic / Reserved_Bandwidth，若 Actual_Traffic 平均为 10 Mbps，Reserved 为 16.67 Mbps，则 Utilization ≈ 60%，剩余 40% 带宽为闲置资源，需评估是否可复用或降级

## Evidence

先验知识/题面给定，逻辑校验通过：10/16.67 ≈ 0.5998 ≈ 60%，剩余 40% 计算正确，定义符合带宽利用率基本逻辑。
