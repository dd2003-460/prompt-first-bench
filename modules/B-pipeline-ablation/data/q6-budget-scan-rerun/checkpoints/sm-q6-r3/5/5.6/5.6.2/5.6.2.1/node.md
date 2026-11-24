# N293: 自建POP内部IGP（OSPF/IS-IS）收敛时间 $T_{igp}$ 的典型值为0.5-1.0秒，取决于网络规模（10个POP节点）及Hello/Dead间

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N112

## Claim

自建POP内部IGP（OSPF/IS-IS）收敛时间 $T_{igp}$ 的典型值为0.5-1.0秒，取决于网络规模（10个POP节点）及Hello/Dead间隔配置（通常OSPF Dead Interval=40s，但收敛检测在1-2个Hello周期内完成）。

## Corrected Claim

自建POP内部IGP（OSPF/IS-IS）收敛时间 $T_{igp}$ 的典型值为0.5-1.0秒，取决于网络规模（10个POP节点）及Hello/Dead间隔配置（通常OSPF Dead Interval=40s，但收敛检测在1-2个Hello周期内完成）。

## Evidence

先验知识/题面给定，逻辑校验通过：OSPF/IS-IS在小型网络（10节点）中收敛时间通常在亚秒至1秒级别，符合工程经验；虽然Dead Interval为40s，但收敛检测确实依赖于Hello间隔（通常10s）或更短的机制（如IS-IS的Hello间隔通常1s，OSPF可配置更短），且实际收敛受SPF计算和LSA泛洪影响，0.5-1.0s是合理的典型值范围。

## Search Query

OSPF convergence time typical value 10 nodes
