# N202: P99 连接建立延迟还需加上 TLS 握手延迟，TLS 1.3 单次往返（1-RTT）约增加 10-20ms，若启用 0-RTT 可忽略，但需考虑证书验证和密钥

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N58

## Claim

P99 连接建立延迟还需加上 TLS 握手延迟，TLS 1.3 单次往返（1-RTT）约增加 10-20ms，若启用 0-RTT 可忽略，但需考虑证书验证和密钥交换的计算开销（约 1-2ms）。

## Corrected Claim

P99 连接建立延迟还需加上 TLS 握手延迟，TLS 1.3 单次往返（1-RTT）约增加 10-20ms，若启用 0-RTT 可忽略，但需考虑证书验证和密钥交换的计算开销（约 1-2ms）。

## Evidence

先验知识/题面给定，逻辑校验通过

## Search Query

TLS 1.3 handshake latency overhead ms
