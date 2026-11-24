# N154: 数据量 < 100TB 且 IOPS > 100,000：本地 NVMe 阵列单位成本虽高，但无需云出口流量费和请求费，且延迟最低 (<1ms)，在极小数据量+

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N40

## Claim

数据量 < 100TB 且 IOPS > 100,000：本地 NVMe 阵列单位成本虽高，但无需云出口流量费和请求费，且延迟最低 (<1ms)，在极小数据量+极高 IOPS 场景下，NVMe 可能因避免云 API 限流和出口费用而具备综合优势。

## Corrected Claim

数据量 < 100TB 且 IOPS > 100,000：本地 NVMe 阵列单位成本虽高，但无需云出口流量费和请求费，且延迟最低 (<1ms)，在极小数据量+极高 IOPS 场景下，NVMe 可能因避免云 API 限流和出口费用而具备综合优势。

## Evidence

先验知识/题面给定，逻辑校验通过：本地NVMe确实无云出口流量费和请求费，且延迟低于1ms，在极高IOPS场景下避免云API限流符合技术常识。
