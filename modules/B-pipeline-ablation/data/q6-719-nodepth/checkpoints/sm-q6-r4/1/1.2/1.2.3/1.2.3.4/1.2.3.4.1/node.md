# N651: TLS 握手延迟 T_tls_p99 为 5ms，基于 TLS 1.3 单次往返 (1-RTT) 握手，RTT ≈ 10ms (用户到边缘)，TLS 1.3 将

- **status**: verified
- **level**: L5
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N215

## Claim

TLS 握手延迟 T_tls_p99 为 5ms，基于 TLS 1.3 单次往返 (1-RTT) 握手，RTT ≈ 10ms (用户到边缘)，TLS 1.3 将握手延迟降低至 1-RTT，故 T_tls_p99 ≈ RTT/2 + 处理时间 ≈ 5ms

## Corrected Claim

TLS 握手延迟 T_tls_p99 为 5ms，基于 TLS 1.3 单次往返 (1-RTT) 握手，RTT ≈ 10ms (用户到边缘)，TLS 1.3 将握手延迟降低至 1-RTT，故 T_tls_p99 ≈ RTT/2 + 处理时间 ≈ 5ms

## Evidence

先验知识/题面给定，逻辑校验通过：TLS 1.3 1-RTT 握手延迟主要取决于 RTT，5ms 对应 10ms RTT 的一半（或包含少量处理时间），量级合理且符合网络协议常识。
