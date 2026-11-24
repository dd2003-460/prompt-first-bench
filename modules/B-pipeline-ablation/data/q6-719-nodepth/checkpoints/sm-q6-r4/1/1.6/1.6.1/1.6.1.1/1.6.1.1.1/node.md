# N567: TLS 1.3 Full Handshake 的最小 RTT 开销为 1 RTT，其计算基础是 ClientHello 消息必须包含 mandatory 的 '

- **status**: verified
- **level**: L5
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N194

## Claim

TLS 1.3 Full Handshake 的最小 RTT 开销为 1 RTT，其计算基础是 ClientHello 消息必须包含 mandatory 的 'key_share' 扩展（ECDSA P-256 或 X25519），使得 ServerHello 能直接完成密钥推导，无需额外的 ChangeCipherSpec 往返。

## Corrected Claim

TLS 1.3 Full Handshake 的最小 RTT 开销为 1 RTT，其计算基础是 ClientHello 消息必须包含 mandatory 的 'key_share' 扩展（ECDSA P-256 或 X25519），使得 ServerHello 能直接完成密钥推导，无需额外的 ChangeCipherSpec 往返。

## Evidence

先验知识/题面给定，逻辑校验通过：TLS 1.3 协议设计核心即为 1-RTT 握手，ClientHello 携带 key_share 允许 ServerHello 直接完成密钥协商，且移除了 ChangeCipherSpec 消息，符合 RFC 8446 规范。

## Search Query

TLS 1.3 full handshake 1 RTT key_share extension RFC 8446
