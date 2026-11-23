# N282: 按峰值带宽计费成本 C_bandwidth_peak = P95_Bandwidth_Mbps * p_peak_per_mbps，其中 P95_Bandwid

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N93

## Claim

按峰值带宽计费成本 C_bandwidth_peak = P95_Bandwidth_Mbps * p_peak_per_mbps，其中 P95_Bandwidth_Mbps 为月度95分位带宽（需根据日均2TB下载量及突发系数估算，典型值约500-1000Mbps），p_peak_per_mbps 为运营商或云厂商的峰值单价（通常¥50-150/Mbps/月，具体依合同阶梯定价而定）

## Corrected Claim

按峰值带宽计费成本 C_bandwidth_peak = P95_Bandwidth_Mbps * p_peak_per_mbps，其中 P95_Bandwidth_Mbps 为月度95分位带宽（需根据日均2TB下载量及突发系数估算，典型值约500-1000Mbps），p_peak_per_mbps 为运营商或云厂商的峰值单价（通常¥50-150/Mbps/月，具体依合同阶梯定价而定）

## Evidence

先验知识/题面给定，逻辑校验通过：公式结构符合带宽计费常识，P95带宽估算（2TB/天约需500Mbps基础带宽，考虑突发系数后500-1000Mbps合理）及单价区间（¥50-150/Mbps/月）符合市场典型量级，无内部矛盾。

## Search Query

cloud CDN peak bandwidth pricing per Mbps monthly
