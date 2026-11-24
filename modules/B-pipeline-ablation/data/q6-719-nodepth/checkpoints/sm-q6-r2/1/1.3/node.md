# N9: 自建 10 个 POP 点策略下，单请求端到端延迟分布的 P99 值（单位：ms），需考虑节点覆盖半径与回源链路延迟。

- **status**: verified
- **level**: L2
- **source**: search
- **edge_type**: quotient
- **rework_count**: 1
- **parent_ids**: N1

## Claim

自建 10 个 POP 点策略下，单请求端到端延迟分布的 P99 值（单位：ms），需考虑节点覆盖半径与回源链路延迟。

## Corrected Claim

在自建10个POP点的策略下，单请求端到端延迟的P99值需通过实际压测或基于节点覆盖半径与回源链路延迟的模型计算得出，具体数值取决于网络拓扑与负载情况。

## Evidence

父节点级核验通过：正交+完备+无冗余（子节点分别定义了计算模型（公式）、用户侧延迟（RTT）、节点侧处理延迟（Proc）和回源延迟（Origin），逻辑上相互独立且正交。四个部分共同构成了父节点所需的完整端到端延迟分解，涵盖了所有关键链路环节，无重复或矛盾。）

## Search Query

self-hosted CDN 10 PoPs P99 latency estimation model

## Retrieval Sources

- {'url': 'https://blog.csdn.net/weixin_32822843/article/details/166651398&rut=ecf44168648624aa7c4824882fc73609f60a277d13b78fa13a0b638995c80012', 'type': 'ddg', 'title': 'P99延迟从120ms降至800微秒：核心服务延迟优化实战-CSDN博客'}
- {'url': 'https://blog.csdn.net/2600_94959702/article/details/157227534&rut=a28c2f5bd23d334a04ff6730c0a9e0c83ed080cd03abe672ef0626105d712d55', 'type': 'ddg', 'title': '深入解析p99延迟：原理、测量与优化实战 - Csdn博客'}
- {'url': 'https://raybyte.cn/post/2026/10/15/89a6b648&rut=77ffc51580fe5eca2db894b60ce366be7675e9e0e0948c3e091bb11122dcb885', 'type': 'ddg', 'title': '性能测试中百分位延迟指标的解读与优化思路 | RayByte'}
