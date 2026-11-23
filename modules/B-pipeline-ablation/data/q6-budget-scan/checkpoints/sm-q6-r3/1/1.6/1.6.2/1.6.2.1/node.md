# N216: 公有云CDN回源路径中TCP/TLS握手延迟的量化：T_handshake_origin = 2 * RTT_edge_to_origin + T_tls_ha

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N67

## Claim

公有云CDN回源路径中TCP/TLS握手延迟的量化：T_handshake_origin = 2 * RTT_edge_to_origin + T_tls_handshake，其中T_tls_handshake取决于TLS版本（TLS 1.2为2-RTT，TLS 1.3为1-RTT，Session Resumption可降至0-RTT），若未启用HTTP/3或QUIC，额外增加1-2个RTT，需评估对P99延迟的具体贡献（通常5-20ms）

## Corrected Claim

公有云CDN回源路径中TCP/TLS握手延迟的量化：T_handshake_origin = 2 * RTT_edge_to_origin + T_tls_handshake，其中T_tls_handshake取决于TLS版本（TLS 1.2为2-RTT，TLS 1.3为1-RTT，Session Resumption可降至0-RTT），若未启用HTTP/3或QUIC，额外增加1-2个RTT，需评估对P99延迟的具体贡献（通常5-20ms）

## Evidence

先验知识/题面给定，逻辑校验通过：TLS 1.2/1.3握手RTT数符合协议标准，QUIC/HTTP3特性描述准确，5-20ms的P99延迟贡献在典型公网RTT（10-50ms）下量级合理。

## Search Query

TLS 1.3 handshake latency RTT reduction HTTP/3 QUIC origin fetch overhead
