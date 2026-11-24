# N327: TLS 1.3 握手延迟 T_tls_handshake = 1 RTT (Full Handshake) 或 0 RTT (Session Resumptio

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N102

## Claim

TLS 1.3 握手延迟 T_tls_handshake = 1 RTT (Full Handshake) 或 0 RTT (Session Resumption)，P99 延迟中需区分新会话与复用会话的比例 R_resume，T_tls_avg = (1-R_resume)*1RTT + R_resume*0RTT。

## Corrected Claim

TLS 1.3 握手延迟 T_tls_handshake = 1 RTT (Full Handshake) 或 0 RTT (Session Resumption)，P99 延迟中需区分新会话与复用会话的比例 R_resume，T_tls_avg = (1-R_resume)*1RTT + R_resume*0RTT。

## Evidence

先验知识/题面给定，逻辑校验通过：TLS 1.3 标准规定完整握手为 1-RTT，会话复用（0-RTT）为 0-RTT，加权平均公式逻辑自洽且符合协议规范。
