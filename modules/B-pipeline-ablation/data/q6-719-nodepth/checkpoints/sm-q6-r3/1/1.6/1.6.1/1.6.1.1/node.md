# N194: TLS 1.3 标准握手（Full Handshake）确实只需 1 RTT 完成密钥交换和证书验证，因为 ClientHello 包含 key_share，S

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N56

## Claim

TLS 1.3 标准握手（Full Handshake）确实只需 1 RTT 完成密钥交换和证书验证，因为 ClientHello 包含 key_share，ServerHello 包含 server key share 和证书，无需额外的 ChangeCipherSpec 往返。

## Corrected Claim

TLS 1.3 标准握手（Full Handshake）确实只需 1 RTT 完成密钥交换和证书验证，因为 ClientHello 包含 key_share，ServerHello 包含 server key share 和证书，无需额外的 ChangeCipherSpec 往返。

## Evidence

先验知识/题面给定，逻辑校验通过
