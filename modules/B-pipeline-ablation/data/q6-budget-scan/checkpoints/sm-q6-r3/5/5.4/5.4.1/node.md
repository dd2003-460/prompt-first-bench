# N178: 图片首屏网络延迟预算上限 = P99总延迟预算(300ms) - RTT(20ms) - T_proc(5ms) - 对象传输时间(500KB/10Mbps=4

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N55

## Claim

图片首屏网络延迟预算上限 = P99总延迟预算(300ms) - RTT(20ms) - T_proc(5ms) - 对象传输时间(500KB/10Mbps=400ms)；若对象传输时间超过剩余预算，则需启用分片加载或预加载策略，否则网络延迟本身无法独立满足SLO，必须将对象传输时间计入CDN优化范围。

## Corrected Claim

图片首屏网络延迟预算上限 = P99总延迟预算(300ms) - RTT(20ms) - T_proc(5ms) - 对象传输时间(500KB/10Mbps=400ms)；若对象传输时间超过剩余预算，则需启用分片加载或预加载策略，否则网络延迟本身无法独立满足SLO，必须将对象传输时间计入CDN优化范围。

## Evidence

先验知识/题面给定，逻辑校验通过：算术运算正确（300-20-5-400=-125ms），结论符合网络延迟预算分配的基本逻辑，即当传输时间超出剩余预算时，必须通过优化传输（如CDN、分片）来满足SLO。
