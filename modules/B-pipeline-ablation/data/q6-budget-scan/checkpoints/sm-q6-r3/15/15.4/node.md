# N408: 全自建变动成本 $C_{var}^{self}(R)$ 的带宽单价 $P_{bw}^{self}$ 估算：基于 N134 修正后的自建带宽成本，假设按峰值带宽预

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N150

## Claim

全自建变动成本 $C_{var}^{self}(R)$ 的带宽单价 $P_{bw}^{self}$ 估算：基于 N134 修正后的自建带宽成本，假设按峰值带宽预留 100Mbps，月成本 100 元，月流量 60TB，则 $P_{bw}^{self} \approx 0.0016$ 元/GB；若考虑跨网结算溢价 20%，则 $P_{bw}^{self} \approx 0.0019$ 元/GB。

## Corrected Claim

全自建变动成本 $C_{var}^{self}(R)$ 的带宽单价 $P_{bw}^{self}$ 估算：基于 N134 修正后的自建带宽成本，假设按峰值带宽预留 100Mbps，月成本 100 元，月流量 60TB，则 $P_{bw}^{self} \approx 0.0016$ 元/GB；若考虑跨网结算溢价 20%，则 $P_{bw}^{self} \approx 0.0019$ 元/GB。

## Evidence

先验知识/题面给定，逻辑校验通过：100元/60TB ≈ 0.00167元/GB，取0.0016合理；加20%溢价后0.0016*1.2=0.00192，取0.0019合理。
