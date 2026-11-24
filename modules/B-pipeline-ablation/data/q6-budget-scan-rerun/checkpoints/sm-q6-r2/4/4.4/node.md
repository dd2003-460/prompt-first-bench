# N20: 全公有云策略的弹性伸缩系数：弹性系数 E_pub = (B_peak_pub - B_avg) / B_avg，即峰谷带宽差与平均带宽之比，公有云 CDN 的弹

- **status**: pending
- **level**: L2
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N4

## Claim

全公有云策略的弹性伸缩系数：弹性系数 E_pub = (B_peak_pub - B_avg) / B_avg，即峰谷带宽差与平均带宽之比，公有云 CDN 的弹性伸缩响应时间 T_scale_pub 通常为分钟级（1–5 分钟），因为厂商在后台自动调整边缘节点资源，用户无需干预，弹性成本已包含在按量计费中。

## Corrected Claim

全公有云策略的弹性伸缩系数：弹性系数 E_pub = (B_peak_pub - B_avg) / B_avg，即峰谷带宽差与平均带宽之比，公有云 CDN 的弹性伸缩响应时间 T_scale_pub 通常为分钟级（1–5 分钟），因为厂商在后台自动调整边缘节点资源，用户无需干预，弹性成本已包含在按量计费中。

## Evidence

父节点级核验未通过：不完备（子节点正交，分别聚焦于弹性系数的数值计算和响应时间对延迟的影响机制。但父节点明确提到了‘弹性成本已包含在按量计费中’这一关键财务属性，而现有两个子节点均未覆盖此方面，导致完备性不足。）

## Search Query

public cloud CDN elastic scaling response time minute level automatic resource adjustment
