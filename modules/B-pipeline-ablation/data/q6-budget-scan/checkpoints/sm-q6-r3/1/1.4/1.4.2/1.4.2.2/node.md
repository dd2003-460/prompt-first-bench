# N146: TLS会话复用（Session Resumption）节省时间 t_reuse 的计算：若启用 Session ID 或 Session Ticket，t_re

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N42

## Claim

TLS会话复用（Session Resumption）节省时间 t_reuse 的计算：若启用 Session ID 或 Session Ticket，t_reuse = t_handshake - (1 * RTT + t_cert_verify)，即节省 1-RTT 和证书验证时间，典型节省 20-50ms，复用率 r_resume 通常 > 90%。

## Corrected Claim

TLS会话复用（Session Resumption）节省时间 t_reuse 的计算：若启用 Session ID 或 Session Ticket，t_reuse = t_handshake - (1 * RTT + t_cert_verify)，即节省 1-RTT 和证书验证时间，典型节省 20-50ms，复用率 r_resume 通常 > 90%。

## Evidence

先验知识/题面给定，逻辑校验通过
