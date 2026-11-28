# N682: TLS 1.3 握手在跨数据中心（RTT≈50ms）环境下的 T_reconnect_handshake 典型值为 2*RTT + 加密协商时间 ≈ 100ms

- **status**: verified
- **level**: L5
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N247

## Claim

TLS 1.3 握手在跨数据中心（RTT≈50ms）环境下的 T_reconnect_handshake 典型值为 2*RTT + 加密协商时间 ≈ 100ms + 20ms = 120ms，加上 API 认证（OAuth2/JWT 验证）耗时约 50-100ms，总计约 170-220ms，远低于 2s 上限，但需考虑 DNS 解析延迟（首次连接）可能增加 100-300ms

## Corrected Claim

TLS 1.3 握手在跨数据中心（RTT≈50ms）环境下的 T_reconnect_handshake 典型值为 2*RTT + 加密协商时间 ≈ 100ms + 20ms = 120ms，加上 API 认证（OAuth2/JWT 验证）耗时约 50-100ms，总计约 170-220ms，远低于 2s 上限，但需考虑 DNS 解析延迟（首次连接）可能增加 100-300ms

## Evidence

先验知识/题面给定，逻辑校验通过：TLS 1.3 重连握手通常为 1-RTT（约50ms），全握手为 2-RTT（约100ms），加上认证和DNS延迟，总耗时在170-420ms范围内，远低于2s上限，量级合理且符合网络协议常识。

## Search Query

TLS 1.3 handshake latency cross datacenter RTT authentication overhead
