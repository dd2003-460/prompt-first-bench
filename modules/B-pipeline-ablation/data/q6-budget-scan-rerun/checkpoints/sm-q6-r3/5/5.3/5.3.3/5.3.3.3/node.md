# N276: Anycast IP与Unicast IP调度对延迟的影响：自建POP使用Anycast IP时，BGP路由将用户引导至最近POP，延迟 $RTT_{anyca

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N100

## Claim

Anycast IP与Unicast IP调度对延迟的影响：自建POP使用Anycast IP时，BGP路由将用户引导至最近POP，延迟 $RTT_{anycast} = \min_{i} RTT_{user,POP_i}$；公有云CDN使用Unicast IP或Anycast，取决于厂商实现；需量化Anycast路由收敛时间（10-100ms）对初始连接延迟的影响，以及BGP选路算法（AS Path Length, Local Preference）对'最近'定义的偏差（可能选择AS跳数最少而非物理距离最短的POP）

## Corrected Claim

Anycast IP与Unicast IP调度对延迟的影响：自建POP使用Anycast IP时，BGP路由将用户引导至最近POP，延迟 $RTT_{anycast} = \min_{i} RTT_{user,POP_i}$；公有云CDN使用Unicast IP或Anycast，取决于厂商实现；需量化Anycast路由收敛时间（10-100ms）对初始连接延迟的影响，以及BGP选路算法（AS Path Length, Local Preference）对'最近'定义的偏差（可能选择AS跳数最少而非物理距离最短的POP）

## Evidence

先验知识/题面给定，逻辑校验通过：Anycast基于BGP最短AS Path选路，理论上引导至最近POP，但存在收敛延迟及AS跳数与物理距离偏差，符合网络工程常识。
