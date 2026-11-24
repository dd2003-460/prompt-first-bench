# N192: 实际网络RTT通常高于理论最小值，需增加交换机/路由器处理延迟（每跳约0.1-0.5ms，跨域骨干网通常经过3-5跳核心路由器），累计附加延迟约为1-2.5ms

- **status**: degraded
- **level**: L4
- **source**: search
- **edge_type**: quotient
- **rework_count**: 1
- **parent_ids**: N55

## Claim

实际网络RTT通常高于理论最小值，需增加交换机/路由器处理延迟（每跳约0.1-0.5ms，跨域骨干网通常经过3-5跳核心路由器），累计附加延迟约为1-2.5ms/方向。

## Corrected Claim

实际网络RTT通常高于理论最小值，需增加交换机/路由器处理延迟及路由跳数带来的累积延迟，具体数值取决于网络路径和设备性能。

## Evidence

[质询]具体数值（每跳0.1-0.5ms，3-5跳，累计1-2.5ms）属于经验性工程参数，不同网络架构、设备性能及拥塞状态下波动极大，缺乏通用性，且参考来源未提供这些具体数值的直接支持。 | 逻辑自洽（处理延迟叠加符合物理直觉），但参考来源[1][2][3]仅定性讨论RTT构成及影响因素，未提供具体的每跳延迟数值或跳数统计，属于经验事实且缺来源直接支持。

## Search Query

core router processing latency per hop ms backbone network

## Retrieval Sources

- {'url': 'https://blog.csdn.net/solihawk/article/details/129248379&rut=b7fe883f232bfca0322dc9dc238cb810ca241559c0b19883488286e1baf459b8', 'type': 'ddg', 'title': 'TCP中RTT时延的理解_rtt延迟-CSDN博客'}
- {'url': 'https://blog.csdn.net/2601_95872615/article/details/162341802&rut=32a684cb50ca651ffc8a0f47b33448743b3905da244d2e7760fddf3667825c93', 'type': 'ddg', 'title': '国际网络延迟排查实战：为什么千兆宽带访问海外服务仍然有 100ms+？_3000km的rtt是多少-CSDN博客'}
- {'url': 'https://bbs.csdn.net/weixin_30522983/article/details/100287734&rut=02a5558adf2b4aab49fa8edc3058f349c66c3235bc0e2b91054c5365db3c3710', 'type': 'ddg', 'title': '信道延迟全解析：从构成原理到实测排障与优化实践'}
