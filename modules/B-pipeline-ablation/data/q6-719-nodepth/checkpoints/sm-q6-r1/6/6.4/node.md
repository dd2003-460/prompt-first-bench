# N43: 敏感性分析中，平均对象大小 s 的变动对成本的影响：s 从 1MB 增至 5MB 时，带宽成本 C_bandwidth 线性增加，但请求单价 C_request

- **status**: verified
- **level**: L2
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N6

## Claim

敏感性分析中，平均对象大小 s 的变动对成本的影响：s 从 1MB 增至 5MB 时，带宽成本 C_bandwidth 线性增加，但请求单价 C_request 不变，导致公有云CDN的带宽成本占比上升，自建POP的带宽成本占比下降（因自建带宽固定成本占比高）。

## Corrected Claim

敏感性分析中，平均对象大小 s 的变动对成本的影响：s 从 1MB 增至 5MB 时，带宽成本 C_bandwidth 线性增加，但请求单价 C_request 不变，导致公有云CDN的带宽成本占比上升，自建POP的带宽成本占比下降（因自建带宽固定成本占比高）。

## Evidence

先验知识/题面给定，逻辑校验通过：带宽成本与流量（对象大小）成正比，请求成本与次数成正比，对象变大导致带宽成本占比上升，符合CDN计费基本逻辑。
