# N180: 自建POP点协议处理延迟T_protocol：TCP握手（3次RTT）+ TLS握手（2-3次RTT）+ HTTP/2头部压缩；对于长连接，T_protocol

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N49

## Claim

自建POP点协议处理延迟T_protocol：TCP握手（3次RTT）+ TLS握手（2-3次RTT）+ HTTP/2头部压缩；对于长连接，T_protocol ≈ 1-5ms（仅头部处理）；对于新连接，T_protocol = 5 * RTT + 2ms（TLS密钥交换）；P99 T_protocol受连接复用率影响，复用率>90%时，T_protocol_P99 ≈ 5-10ms

## Corrected Claim

自建POP点协议处理延迟T_protocol：TCP握手（3次RTT）+ TLS握手（2-3次RTT）+ HTTP/2头部压缩；对于长连接，T_protocol ≈ 1-5ms（仅头部处理）；对于新连接，T_protocol = 5 * RTT + 2ms（TLS密钥交换）；P99 T_protocol受连接复用率影响，复用率>90%时，T_protocol_P99 ≈ 5-10ms

## Evidence

先验知识/题面给定，逻辑校验通过
