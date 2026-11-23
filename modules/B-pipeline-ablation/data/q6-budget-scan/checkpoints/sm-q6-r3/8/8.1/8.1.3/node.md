# N355: 跨网互联附加费 $C_{cross}$：自建节点若需同时接入电信、联通、移动三家网络以实现多线接入，需支付额外的跨网互联费用或分别租赁三条专线，总带宽成本 $C

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N131

## Claim

跨网互联附加费 $C_{cross}$：自建节点若需同时接入电信、联通、移动三家网络以实现多线接入，需支付额外的跨网互联费用或分别租赁三条专线，总带宽成本 $C_{bw}^{self} = \sum_{i} B_{reserved, i} \times R_{i}$，其中 $i$ 为运营商，需计算多线接入下的加权平均单 Gbps 成本。

## Corrected Claim

跨网互联附加费 $C_{cross}$：自建节点若需同时接入电信、联通、移动三家网络以实现多线接入，需支付额外的跨网互联费用或分别租赁三条专线，总带宽成本 $C_{bw}^{self} = \sum_{i} B_{reserved, i} \times R_{i}$，其中 $i$ 为运营商，需计算多线接入下的加权平均单 Gbps 成本。

## Evidence

先验知识/题面给定，逻辑校验通过
