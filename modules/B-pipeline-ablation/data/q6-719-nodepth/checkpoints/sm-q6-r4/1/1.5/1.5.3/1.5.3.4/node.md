# N192: 实际网络RTT通常高于理论最小值，需增加交换机/路由器处理延迟（每跳约0.1-0.5ms，跨域骨干网通常经过3-5跳核心路由器），累计附加延迟约为1-2.5ms

- **status**: pending
- **level**: L4
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N55

## Claim

实际网络RTT通常高于理论最小值，需增加交换机/路由器处理延迟（每跳约0.1-0.5ms，跨域骨干网通常经过3-5跳核心路由器），累计附加延迟约为1-2.5ms/方向。

## Corrected Claim

实际网络RTT通常高于理论最小值，需增加交换机/路由器处理延迟及路由跳数带来的累积延迟，具体数值取决于网络路径和设备性能。

## Evidence

父节点级核验未通过：非正交, 有冗余（子节点并非正交的概念分解，而是同一物理模型（延迟=跳数×单跳延迟）在参数空间（跳数、单跳延迟）上的三个离散采样点。它们之间存在包含关系（如工作点A是工作点B的子集情况），且本质上是冗余的参数组合，而非独立的知识维度。）

## Search Query

core router processing latency per hop ms backbone network

## Retrieval Sources

- {'url': 'https://blog.csdn.net/solihawk/article/details/129248379&rut=b7fe883f232bfca0322dc9dc238cb810ca241559c0b19883488286e1baf459b8', 'type': 'ddg', 'title': 'TCP中RTT时延的理解_rtt延迟-CSDN博客'}
- {'url': 'https://blog.csdn.net/2601_95872615/article/details/162341802&rut=32a684cb50ca651ffc8a0f47b33448743b3905da244d2e7760fddf3667825c93', 'type': 'ddg', 'title': '国际网络延迟排查实战：为什么千兆宽带访问海外服务仍然有 100ms+？_3000km的rtt是多少-CSDN博客'}
- {'url': 'https://bbs.csdn.net/weixin_30522983/article/details/100287734&rut=02a5558adf2b4aab49fa8edc3058f349c66c3235bc0e2b91054c5365db3c3710', 'type': 'ddg', 'title': '信道延迟全解析：从构成原理到实测排障与优化实践'}
