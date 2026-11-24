# N212: TLS 1.3 握手延迟 P99 为 5ms，基于单次 RTT 完成握手（1-RTT handshake）且边缘节点 CPU 性能充足（Intel Xeon 8

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N54

## Claim

TLS 1.3 握手延迟 P99 为 5ms，基于单次 RTT 完成握手（1-RTT handshake）且边缘节点 CPU 性能充足（Intel Xeon 8380 级别），TLS 加解密开销 < 1ms，主要耗时为网络往返

## Corrected Claim

TLS 1.3 握手延迟 P99 为 5ms，基于单次 RTT 完成握手（1-RTT handshake）且边缘节点 CPU 性能充足（Intel Xeon 8380 级别），TLS 加解密开销 < 1ms，主要耗时为网络往返

## Evidence

先验知识/题面给定，逻辑校验通过：TLS 1.3 1-RTT 握手延迟主要取决于网络 RTT，在边缘节点 CPU 充足且加解密开销 <1ms 的假设下，P99 为 5ms 符合低延迟网络环境的工程直觉。
