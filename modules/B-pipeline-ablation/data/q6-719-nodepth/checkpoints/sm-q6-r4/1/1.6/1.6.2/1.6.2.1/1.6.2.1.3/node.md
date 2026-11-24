# N575: TLS 1.2 Full Handshake 中证书验证的计算开销 T_cert_verify：基于 RSA 2048 公钥加密/解密或 ECDSA P-256

- **status**: verified
- **level**: L5
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N197

## Claim

TLS 1.2 Full Handshake 中证书验证的计算开销 T_cert_verify：基于 RSA 2048 公钥加密/解密或 ECDSA P-256 签名验证的单次耗时（客户端约 5-10ms，服务端约 1-5ms），该开销叠加在 RTT 之上，影响端到端握手总耗时

## Corrected Claim

TLS 1.2 Full Handshake 中证书验证的计算开销 T_cert_verify：基于 RSA 2048 公钥加密/解密或 ECDSA P-256 签名验证的单次耗时（客户端约 5-10ms，服务端约 1-5ms），该开销叠加在 RTT 之上，影响端到端握手总耗时

## Evidence

先验知识/题面给定，逻辑校验通过
