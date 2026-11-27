# N83: 隐性成本对比：2x 消费卡方案需支持双卡插槽的主板 (通常 ATX/E-ATX 高端主板) 和 1000W+ 电源，而 1x A100 SXM4 需服务器级基板

- **status**: degraded
- **level**: L3
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N18

## Claim

隐性成本对比：2x 消费卡方案需支持双卡插槽的主板 (通常 ATX/E-ATX 高端主板) 和 1000W+ 电源，而 1x A100 SXM4 需服务器级基板 (如 Supermicro) 或专用 A100 PCIe 转接卡，需列出这两类基础设施的额外采购成本差值 ΔP_infra = P_infra_2x4090 - P_infra_1xA100。

## Corrected Claim

隐性成本对比：2x 消费卡方案通常需支持双卡插槽的主板 (通常 ATX/E-ATX 高端主板) 和 1000W+ 电源，而 1x A100 SXM4 需服务器级基板 (如 Supermicro) 或专用 A100 PCIe 转接卡。这两类基础设施存在显著的采购成本差异，具体差值 ΔP_infra 需根据实时市场价格计算，通常服务器级基础设施成本高于消费级方案。

## Evidence

[质询]该陈述要求列出具体的基础设施成本差值 ΔP_infra，但参考来源仅提供了定性对比（消费级 vs 服务器级性价比），未提供具体的价格数值或差值计算依据，属于经验事实且缺乏直接数据支持。 | 来源[1]间接支持了双卡方案使用消费级主板/电源、A100方案使用服务器级硬件的逻辑前提，但未提供具体成本数值，无法直接验证 ΔP_infra 的具体值，故降级为定性表述。

## Search Query

cost of dual GPU motherboard 1000W PSU vs A100 SXM4 server chassis infrastructure cost

## Retrieval Sources

- {'url': 'https://zhuanlan.zhihu.com/p/2027319793145921832&rut=e3e7393a54cb5f6d51124d0a6e8afb3f2cc9cfb2207f94de37d1c7fb04555219', 'type': 'ddg', 'title': '分享一个非常不错的双卡方案 - 知乎'}
