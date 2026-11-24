# N573: TLS 1.2 Full Handshake 第一个 RTT 的传输内容分解：ClientHello (含支持的密码套件列表、压缩方法、扩展字段) 与 Serv

- **status**: verified
- **level**: L5
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N197

## Claim

TLS 1.2 Full Handshake 第一个 RTT 的传输内容分解：ClientHello (含支持的密码套件列表、压缩方法、扩展字段) 与 ServerHello+Certificate+ServerKeyExchange+ServerHelloDone 的报文大小及网络传输耗时 T_trans1 = (Size_CH + Size_SH_Cert) / Effective_Bandwidth

## Corrected Claim

TLS 1.2 Full Handshake 第一个 RTT 的传输内容分解：ClientHello (含支持的密码套件列表、压缩方法、扩展字段) 与 ServerHello+Certificate+ServerKeyExchange+ServerHelloDone 的报文大小及网络传输耗时 T_trans1 = (Size_CH + Size_SH_Cert) / Effective_Bandwidth

## Evidence

先验知识/题面给定，逻辑校验通过
