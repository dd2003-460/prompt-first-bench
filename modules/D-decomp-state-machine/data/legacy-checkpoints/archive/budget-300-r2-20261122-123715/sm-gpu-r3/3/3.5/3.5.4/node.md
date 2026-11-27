# N83: 隐性成本对比：2x 消费卡方案需支持双卡插槽的主板 (通常 ATX/E-ATX 高端主板) 和 1000W+ 电源，而 1x A100 SXM4 需服务器级基板

- **status**: verified
- **level**: L3
- **source**: search
- **edge_type**: quotient
- **rework_count**: 1
- **parent_ids**: N18

## Claim

隐性成本对比：2x 消费卡方案需支持双卡插槽的主板 (通常 ATX/E-ATX 高端主板) 和 1000W+ 电源，而 1x A100 SXM4 需服务器级基板 (如 Supermicro) 或专用 A100 PCIe 转接卡，需列出这两类基础设施的额外采购成本差值 ΔP_infra = P_infra_2x4090 - P_infra_1xA100。

## Corrected Claim

隐性成本对比：2x 消费卡方案通常需支持双卡插槽的主板 (通常 ATX/E-ATX 高端主板) 和 1000W+ 电源，而 1x A100 SXM4 需服务器级基板 (如 Supermicro) 或专用 A100 PCIe 转接卡。这两类基础设施存在显著的采购成本差异，具体差值 ΔP_infra 需根据实时市场价格计算，通常服务器级基础设施成本高于消费级方案。

## Evidence

父节点级核验通过：正交+完备+无冗余（子节点逻辑清晰且正交：前两个节点分别独立计算两个方案的基础设施成本，第三个节点基于前两者计算差值并补充SXM4的特殊情况，无重复或矛盾。完备性方面，涵盖了父节点要求列出的两类基础设施及差值计算。虽然第3个节点包含了对前两个节点数据的引用，但这属于推导结果而非冗余定义，且增加了SXM4这一关键变量，因此不视为冗余。）

## Search Query

cost of dual GPU motherboard 1000W PSU vs A100 SXM4 server chassis infrastructure cost

## Retrieval Sources

- {'url': 'https://zhuanlan.zhihu.com/p/2027319793145921832&rut=e3e7393a54cb5f6d51124d0a6e8afb3f2cc9cfb2207f94de37d1c7fb04555219', 'type': 'ddg', 'title': '分享一个非常不错的双卡方案 - 知乎'}
