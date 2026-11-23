# N367: 策略切换决策阈值 ΔC_threshold 的确定：ΔC_threshold = ΔC_self_max - ΔC_cloud_min，其中 ΔC_self_m

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N113

## Claim

策略切换决策阈值 ΔC_threshold 的确定：ΔC_threshold = ΔC_self_max - ΔC_cloud_min，其中 ΔC_self_max 为自建策略最大可接受边际成本，ΔC_cloud_min 为公有云策略最小边际成本；当 ΔC_self < ΔC_cloud 时增加自建，反之增加公有云

## Corrected Claim

策略切换决策阈值 ΔC_threshold 的确定：ΔC_threshold = ΔC_self_max - ΔC_cloud_min，其中 ΔC_self_max 为自建策略最大可接受边际成本，ΔC_cloud_min 为公有云策略最小边际成本；当 ΔC_self < ΔC_cloud 时增加自建，反之增加公有云

## Evidence

先验知识/题面给定，逻辑校验通过
