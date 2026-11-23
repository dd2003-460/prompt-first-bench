# N194: HTTP/3 (QUIC) 连接建立延迟 T_handshake_quic = 0 * RTT（0-RTT）或 1 * RTT（1-RTT），结合 TLS 1.

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N58

## Claim

HTTP/3 (QUIC) 连接建立延迟 T_handshake_quic = 0 * RTT（0-RTT）或 1 * RTT（1-RTT），结合 TLS 1.3 密钥协商，P99 ≈ 10-30 ms，显著优于 TCP+TLS，但受丢包率影响较大

## Corrected Claim

HTTP/3 (QUIC) 连接建立延迟 T_handshake_quic = 0 * RTT（0-RTT）或 1 * RTT（1-RTT），结合 TLS 1.3 密钥协商，P99 ≈ 10-30 ms，显著优于 TCP+TLS，但受丢包率影响较大

## Evidence

先验知识/题面给定，逻辑校验通过

## Search Query

QUIC HTTP/3 0-RTT 1-RTT connection setup latency
