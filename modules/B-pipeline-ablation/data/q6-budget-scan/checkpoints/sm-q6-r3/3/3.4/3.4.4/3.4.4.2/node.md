# N297: P99延迟优化与带宽成本的交互效应：在阶梯计价下，若通过增加边缘节点降低P99延迟导致回源流量减少，从而总流量降至下一阶梯（如从60TB降至45TB），则带宽总

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N92

## Claim

P99延迟优化与带宽成本的交互效应：在阶梯计价下，若通过增加边缘节点降低P99延迟导致回源流量减少，从而总流量降至下一阶梯（如从60TB降至45TB），则带宽总成本下降 ΔCost = (60-45)TB * P_tier3 + 45TB * (P_tier3 - P_tier2)，该离散跳跃式成本节约远高于线性计价模型下的节约，使得延迟优化的ROI在阶梯边界附近被高估

## Corrected Claim

P99延迟优化与带宽成本的交互效应：在阶梯计价下，若通过增加边缘节点降低P99延迟导致回源流量减少，从而总流量降至下一阶梯（如从60TB降至45TB），则带宽总成本下降 ΔCost = (60-45)TB * P_tier3 + 45TB * (P_tier3 - P_tier2)，该离散跳跃式成本节约远高于线性计价模型下的节约，使得延迟优化的ROI在阶梯边界附近被高估

## Evidence

先验知识/题面给定，逻辑校验通过：阶梯计价下跨越阈值导致的成本节约确实包含‘原阶梯单价差’与‘流量减少量’两部分，其离散跳跃特性在数学上高于线性模型的连续节约，逻辑自洽。

## Search Query

CDN cost savings reducing origin fetch tiered pricing
