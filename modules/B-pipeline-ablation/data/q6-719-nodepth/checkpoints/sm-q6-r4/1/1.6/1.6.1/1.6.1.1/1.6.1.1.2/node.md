# N568: 在 Full Handshake 中，ServerHello 携带的 'server key share' 与 ClientHello 中的 'client k

- **status**: verified
- **level**: L5
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N194

## Claim

在 Full Handshake 中，ServerHello 携带的 'server key share' 与 ClientHello 中的 'client key share' 结合，使得 Finished 消息（包含证书验证和握手完整性校验）能在同一 RTT 内完成，该 RTT 的延迟下限由网络传播延迟决定，典型国内骨干网 RTT 为 20-50ms。

## Corrected Claim

在 Full Handshake 中，ServerHello 携带的 'server key share' 与 ClientHello 中的 'client key share' 结合，使得 Finished 消息（包含证书验证和握手完整性校验）能在同一 RTT 内完成，该 RTT 的延迟下限由网络传播延迟决定，典型国内骨干网 RTT 为 20-50ms。

## Evidence

先验知识/题面给定，逻辑校验通过：TLS 1.3 Full Handshake 确实通过 ServerHello 携带 Key Share 实现 1-RTT 完成握手，且国内骨干网 RTT 20-50ms 符合典型网络工程经验值。

## Search Query

TLS 1.3 server hello key share finished message RTT latency
