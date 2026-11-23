# N252: 若自建节点间回源流量走公网互联网，则需支付跨网流量结算费用，典型值为 0.1-0.3 元/GB，这将使回源成本从 0 元/GB 上升至 $C_{backhaul

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N85, N86, N87

## Claim

若自建节点间回源流量走公网互联网，则需支付跨网流量结算费用，典型值为 0.1-0.3 元/GB，这将使回源成本从 0 元/GB 上升至 $C_{backhaul, public} = V_{backhaul} \times P_{settlement}$，显著增加总成本。

## Corrected Claim

若自建节点间回源流量走公网互联网，则需支付跨网流量结算费用，典型值为 0.1-0.3 元/GB，这将使回源成本从 0 元/GB 上升至 $C_{backhaul, public} = V_{backhaul} \times P_{settlement}$，显著增加总成本。

## Evidence

先验知识/题面给定，逻辑校验通过

## Search Query

inter-carrier traffic settlement cost per GB China
