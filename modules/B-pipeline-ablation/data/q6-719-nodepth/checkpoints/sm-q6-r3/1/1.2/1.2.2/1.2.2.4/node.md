# N211: 公有云 CDN 用户到边缘节点 RTT 的 P99 最终估算值为 55ms，计算方式为 max(核心区域 P99 RTT 15ms, 长尾区域 P99 RTT 

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N53

## Claim

公有云 CDN 用户到边缘节点 RTT 的 P99 最终估算值为 55ms，计算方式为 max(核心区域 P99 RTT 15ms, 长尾区域 P99 RTT 40ms) + 跨网惩罚 15ms = 55ms，反映最坏情况下的网络传播延迟

## Corrected Claim

公有云 CDN 用户到边缘节点 RTT 的 P99 最终估算值为 55ms，计算方式为 max(核心区域 P99 RTT 15ms, 长尾区域 P99 RTT 40ms) + 跨网惩罚 15ms = 55ms，反映最坏情况下的网络传播延迟

## Evidence

先验知识/题面给定，逻辑校验通过：计算过程 15+40+15=70 与陈述中的 55ms 存在算术矛盾，但陈述明确给出了公式 max(15, 40) + 15 = 55，其中 max(15,40)=40，40+15=55，算术正确。虽然通常 P99 估算可能涉及更复杂的加权或分布模型，但作为特定场景下的简化估算模型，其内部逻辑自洽且量级（55ms 对于跨网 CDN 边缘节点 RTT P99）符合工程直觉。
