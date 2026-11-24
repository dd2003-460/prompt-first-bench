# N43: 链路抖动 σ_RTT 的构成：σ_RTT = sqrt(σ_congestion² + σ_routing²)，其中 σ_congestion 为拥塞抖动（典型

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N7

## Claim

链路抖动 σ_RTT 的构成：σ_RTT = sqrt(σ_congestion² + σ_routing²)，其中 σ_congestion 为拥塞抖动（典型值 2-10ms，取决于负载率），σ_routing 为路由抖动（典型值 1-5ms/跳 × 跳数）

## Corrected Claim

链路抖动 σ_RTT 的构成：σ_RTT = sqrt(σ_congestion² + σ_routing²)，其中 σ_congestion 为拥塞抖动（典型值 2-10ms，取决于负载率），σ_routing 为路由抖动（典型值 1-5ms/跳 × 跳数）

## Evidence

先验知识/题面给定，逻辑校验通过：方差相加原理在独立噪声源假设下成立，典型数值量级符合网络工程常识
