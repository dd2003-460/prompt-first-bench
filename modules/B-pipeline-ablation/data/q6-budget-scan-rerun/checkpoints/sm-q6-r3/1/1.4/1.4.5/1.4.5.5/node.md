# N233: 峰值期回源延迟惩罚：由于回源请求增加，源站负载上升，假设源站响应时间 T_origin 从 50ms 增至 80ms（线性负载模型），则峰值期 P99 延迟中回

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N60, N61, N62

## Claim

峰值期回源延迟惩罚：由于回源请求增加，源站负载上升，假设源站响应时间 T_origin 从 50ms 增至 80ms（线性负载模型），则峰值期 P99 延迟中回源分量的贡献增加 (80-50) * (1-H_peak) * P99_weight，需纳入总 P99 模型。

## Corrected Claim

峰值期回源延迟惩罚：由于回源请求增加，源站负载上升，假设源站响应时间 T_origin 从 50ms 增至 80ms（线性负载模型），则峰值期 P99 延迟中回源分量的贡献增加 (80-50) * (1-H_peak) * P99_weight，需纳入总 P99 模型。

## Evidence

先验知识/题面给定，逻辑校验通过：延迟增量计算符合线性叠加原理，量纲与逻辑自洽。

## Search Query

origin server latency increase under peak load cache miss impact
