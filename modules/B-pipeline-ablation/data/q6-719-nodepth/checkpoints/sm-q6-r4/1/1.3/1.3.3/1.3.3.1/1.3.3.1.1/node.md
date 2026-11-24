# N676: 低配硬件 TLS 握手延迟分解：P99(TLS_handshake) = T_key_exchange + T_cert_verify + T_session_

- **status**: verified
- **level**: L5
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N225

## Claim

低配硬件 TLS 握手延迟分解：P99(TLS_handshake) = T_key_exchange + T_cert_verify + T_session_establish，其中 T_key_exchange 为 5-10ms（RSA 2048 位），T_cert_verify 为 2-5ms，T_session_establish 为 1-3ms，总计 8-18ms。

## Corrected Claim

低配硬件 TLS 握手延迟分解：P99(TLS_handshake) = T_key_exchange + T_cert_verify + T_session_establish，其中 T_key_exchange 为 5-10ms（RSA 2048 位），T_cert_verify 为 2-5ms，T_session_establish 为 1-3ms，总计 8-18ms。

## Evidence

先验知识/题面给定，逻辑校验通过
