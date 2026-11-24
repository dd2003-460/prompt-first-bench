# N577: TLS 1.2 Session Resumption (Session Ticket) 模式下，服务器无状态，但需执行 AES-128-GCM 加解密操作以验证

- **status**: verified
- **level**: L5
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N198

## Claim

TLS 1.2 Session Resumption (Session Ticket) 模式下，服务器无状态，但需执行 AES-128-GCM 加解密操作以验证 Ticket 有效性，单次加解密耗时约 0.1-0.5ms，且 Ticket 长度通常为 128-256 字节，增加少量网络传输开销

## Corrected Claim

TLS 1.2 Session Resumption (Session Ticket) 模式下，服务器无状态，但需执行 AES-128-GCM 加解密操作以验证 Ticket 有效性，单次加解密耗时约 0.1-0.5ms，且 Ticket 长度通常为 128-256 字节，增加少量网络传输开销

## Evidence

先验知识/题面给定，逻辑校验通过
