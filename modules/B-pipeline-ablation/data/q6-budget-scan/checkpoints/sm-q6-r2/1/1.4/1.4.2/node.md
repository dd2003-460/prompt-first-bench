# N42: TLS握手延迟 t_tls = t_handshake + t_reuse，其中 t_handshake 为完整握手耗时（典型 100-200ms），t_reu

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N9

## Claim

TLS握手延迟 t_tls = t_handshake + t_reuse，其中 t_handshake 为完整握手耗时（典型 100-200ms），t_reuse 为会话复用节省时间（若启用Session Resumption，t_reuse ≈ t_handshake）；在混合策略中，若自建POP与公有云CDN证书不同，每次路由切换可能触发重新握手。

## Corrected Claim

TLS握手延迟 t_tls = t_handshake + t_reuse，其中 t_handshake 为完整握手耗时（典型 100-200ms），t_reuse 为会话复用节省时间（若启用Session Resumption，t_reuse ≈ t_handshake）；在混合策略中，若自建POP与公有云CDN证书不同，每次路由切换可能触发重新握手。

## Evidence

先验知识/题面给定，逻辑校验通过

## Search Query

TLS handshake latency ms
