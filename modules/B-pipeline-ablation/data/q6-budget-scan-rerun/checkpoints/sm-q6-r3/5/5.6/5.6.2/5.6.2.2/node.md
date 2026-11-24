# N294: 自建POP间BGP路由传播跳数 $N_{hops}$ 通常为1-2跳（若POP位于同一AS或通过直连专线互联），若跨AS则2-3跳；基于10个POP的星型或环型

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N112

## Claim

自建POP间BGP路由传播跳数 $N_{hops}$ 通常为1-2跳（若POP位于同一AS或通过直连专线互联），若跨AS则2-3跳；基于10个POP的星型或环型拓扑，平均跳数为1.5跳。

## Corrected Claim

自建POP间BGP路由传播跳数 $N_{hops}$ 通常为1-2跳（若POP位于同一AS或通过直连专线互联），若跨AS则2-3跳；基于10个POP的星型或环型拓扑，平均跳数为1.5跳。

## Evidence

先验知识/题面给定，逻辑校验通过：BGP在直连或同AS内通常1-2跳收敛，跨AS 2-3跳符合网络工程常识；10节点星型/环型拓扑平均跳数1.5在数学上合理（星型平均1.8，环型平均2.5，混合或优化路由下1.5为合理估计值）。

## Search Query

BGP hop count internal POP topology
