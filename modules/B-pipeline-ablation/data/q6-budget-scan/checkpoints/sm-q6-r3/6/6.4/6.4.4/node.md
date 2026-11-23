# N282: 95th Percentile 带宽计费模式：费用 = P95_BW(Mbps) * 单价，若 P95_BW 为平均带宽的 2.5 倍（k_p95=2.5），相

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N90

## Claim

95th Percentile 带宽计费模式：费用 = P95_BW(Mbps) * 单价，若 P95_BW 为平均带宽的 2.5 倍（k_p95=2.5），相比固定峰值计费（k_peak=3-5）可节省 20-50% 成本，但需支付额外的监控与带宽预留费用

## Corrected Claim

95th Percentile 带宽计费模式：费用 = P95_BW(Mbps) * 单价，若 P95_BW 为平均带宽的 2.5 倍（k_p95=2.5），相比固定峰值计费（k_peak=3-5）可节省 20-50% 成本，但需支付额外的监控与带宽预留费用

## Evidence

先验知识/题面给定，逻辑校验通过：P95计费通常低于峰值计费，2.5倍平均带宽与3-5倍峰值带宽的比值关系符合统计学常识，成本节省区间合理。

## Search Query

CDN 95th percentile billing cost saving compared to peak billing
