# N197: TLS 1.2 Full Handshake 需要 2 RTT：第一个 RTT 用于 ClientHello 和 ServerHello+Certificate

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N57

## Claim

TLS 1.2 Full Handshake 需要 2 RTT：第一个 RTT 用于 ClientHello 和 ServerHello+Certificate+ServerKeyExchange，第二个 RTT 用于 ClientKeyExchange+Finished 和 Server Finished。

## Corrected Claim

TLS 1.2 Full Handshake 需要 2 RTT：第一个 RTT 用于 ClientHello 和 ServerHello+Certificate+ServerKeyExchange，第二个 RTT 用于 ClientKeyExchange+Finished 和 Server Finished。

## Evidence

先验知识/题面给定，逻辑校验通过
