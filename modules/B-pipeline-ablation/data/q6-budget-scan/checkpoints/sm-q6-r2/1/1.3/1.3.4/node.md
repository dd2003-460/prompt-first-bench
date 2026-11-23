# N48: 混合策略下，核心区域用户到自建 POP 的跳数 N_hops_hybrid_core 与长尾区域用户到公有云节点的跳数 N_hops_hybrid_tail，用

- **status**: degraded
- **level**: L3
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N8

## Claim

混合策略下，核心区域用户到自建 POP 的跳数 N_hops_hybrid_core 与长尾区域用户到公有云节点的跳数 N_hops_hybrid_tail，用于计算加权网络延迟 L_net_hybrid = 0.65 * (N_hops_hybrid_core * 1.0) + 0.35 * (N_hops_hybrid_tail * 1.0)。

## Corrected Claim

混合策略下，网络延迟 L_net_hybrid 可通过核心区域用户到自建 POP 的跳数与长尾区域用户到公有云节点的跳数加权计算得出，具体权重和单跳延迟需依据实际网络拓扑及业务分布确定。

## Evidence

[质询]该陈述包含具体的经验参数（权重0.65/0.35、每跳延迟1.0ms），这些数值并非第一性原理可推导，且参考来源仅描述POP组网拓扑，未提供具体的跳数或延迟计算模型，存在参数来源不明或口径混淆的风险。 | 逻辑自洽（加权平均公式结构合理），但参考来源[1]仅涉及POP组网概念，未直接支持具体的跳数数值或延迟权重参数，属于经验事实且缺乏直接来源支持。

## Search Query

Hybrid CDN core region self-built POP hops vs tail region cloud hops

## Retrieval Sources

- {'url': 'https://www.h3c.com/cn/pub/Document_Center/2025/09/WebHelp_AD_WAN_FZFAGZCLSC/html/topic_634221.html&rut=996762c841ce3ec8fec2969e554de599f1e3f33747ff375cbb4c6a78eecc76f2', 'type': 'ddg', 'title': '多租户pop组网（Msp运营组网） - H3c'}
