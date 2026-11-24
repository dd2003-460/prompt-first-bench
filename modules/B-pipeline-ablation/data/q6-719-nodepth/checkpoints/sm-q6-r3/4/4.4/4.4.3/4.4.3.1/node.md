# N368: L1 到 L2 的回源延迟 RTT_L1_L2 在自建架构下通常为 10-30ms，取决于 L1 POP 与中心 L2 节点间的物理距离（省内 5-10ms，跨

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N114

## Claim

L1 到 L2 的回源延迟 RTT_L1_L2 在自建架构下通常为 10-30ms，取决于 L1 POP 与中心 L2 节点间的物理距离（省内 5-10ms，跨省 20-30ms）；在公有云架构下，由于内部骨干网优化，RTT_L1_L2 通常稳定在 5-15ms。

## Corrected Claim

L1 到 L2 的回源延迟 RTT_L1_L2 在自建架构下通常为 10-30ms，取决于 L1 POP 与中心 L2 节点间的物理距离（省内 5-10ms，跨省 20-30ms）；在公有云架构下，由于内部骨干网优化，RTT_L1_L2 通常稳定在 5-15ms。

## Evidence

先验知识/题面给定，逻辑校验通过：光信号在光纤中传播速度约为200,000 km/s，单程1ms对应约200km距离。省内距离（<500km）对应RTT 5-10ms，跨省距离（1000-3000km）对应RTT 20-30ms，符合物理规律；公有云骨干网通常采用更短路径或更高带宽优化，延迟略低（5-15ms）也符合工程常识。

## Search Query

CDN L1 to L2 latency backbone network China
