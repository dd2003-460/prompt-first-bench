# N211: 公有云 CDN 用户到边缘节点 RTT 的 P99 最终估算值为 55ms，计算方式为 max(核心区域 P99 RTT 15ms, 长尾区域 P99 RTT 

- **status**: pending
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

父节点级核验未通过：不完备, 有冗余（子节点描述了两个不同区域（核心/长尾）的延迟构成，彼此正交且不矛盾。但是，父节点明确提到的“跨网惩罚 15ms”在子节点中完全缺失，导致子节点之和无法还原父节点的最终估算值，存在信息缺失（不完备）。此外，两个子节点本质上是同一类参数（不同距离/区域下的RTT组成）的两个具体取值，结构上高度重复，属于冗余。）
