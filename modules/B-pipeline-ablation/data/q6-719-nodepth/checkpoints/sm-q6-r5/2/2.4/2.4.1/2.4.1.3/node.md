# N187: L1/L2/L3 运营商网络层级对跳数的影响：L1（骨干）单跳覆盖 1000km+，L2（城域）覆盖 100km，L3（接入）覆盖 10km；跨运营商回源通常增

- **status**: pending
- **level**: L4
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N59

## Claim

L1/L2/L3 运营商网络层级对跳数的影响：L1（骨干）单跳覆盖 1000km+，L2（城域）覆盖 100km，L3（接入）覆盖 10km；跨运营商回源通常增加 1-2 个 AS 跳数，导致 Hops_edge_to_origin 从 3 跳增至 4-5 跳，延迟增加 10-20ms。

## Corrected Claim

L1（骨干）、L2（城域）、L3（接入）是运营商网络拓扑的常见层级划分。跨运营商回源通常因涉及不同自治系统（AS）而增加1-2个路由跳数，导致端到端延迟增加，具体数值取决于网络架构和地理距离。

## Evidence

父节点级核验未通过：不完备, 有冗余（1. 冗余性高：三个子节点本质上是同一物理路径模型（AS_Hops）在不同跳数下的参数化实例，而非独立的正交概念维度，应合并为公式或表格。2. 不完备：父节点明确指出了L1/L2/L3的覆盖半径（1000km/100km/10km）这一关键物理维度，但子节点完全忽略了这一维度，仅讨论了AS跳数，导致分解丢失了父节点中关于地理层级对跳数影响的核心信息。）

## Search Query

ISP hierarchy L1 L2 L3 network latency impact cross-carrier

## Retrieval Sources

- {'url': 'https://zhuanlan.zhihu.com/p/1948433520193143849&rut=12098be41c43a644f008129c403a36ead16bdd43149455122a1ba989c2a94737', 'type': 'ddg', 'title': '5G无缝移动性演进：从L3切换到L1/L2触发机制的深度解析与Release18优化'}
