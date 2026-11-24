# N227: 工作点1（高性低成）：采用同省/同城BGP专线接入，RTT_pop_origin_p99 ≈ 5-10ms，带宽成本 C_bandwidth_per_GB ≈ 

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N59

## Claim

工作点1（高性低成）：采用同省/同城BGP专线接入，RTT_pop_origin_p99 ≈ 5-10ms，带宽成本 C_bandwidth_per_GB ≈ ¥0.15/GB，总 P99(T_origin_fetch_self) ≈ 10-20ms，满足 T=100ms 约束。

## Corrected Claim

工作点1（高性低成）：采用同省/同城BGP专线接入，RTT_pop_origin_p99 ≈ 5-10ms，带宽成本 C_bandwidth_per_GB ≈ ¥0.15/GB，总 P99(T_origin_fetch_self) ≈ 10-20ms，满足 T=100ms 约束。

## Evidence

先验知识/题面给定，逻辑校验通过：同省/同城BGP专线RTT 5-10ms及带宽成本¥0.15/GB符合国内网络工程常识，总延迟10-20ms满足100ms约束，数值量级合理且自洽。
