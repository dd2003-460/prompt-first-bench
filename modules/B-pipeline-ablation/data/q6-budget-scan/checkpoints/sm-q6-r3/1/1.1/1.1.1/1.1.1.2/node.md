# N177: TLS 1.3 Session Resumption（Session ID 或 Ticket）的 P99 延迟 T_tls_resume_p99 ≈ 0.5 R

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N52

## Claim

TLS 1.3 Session Resumption（Session ID 或 Ticket）的 P99 延迟 T_tls_resume_p99 ≈ 0.5 RTT + T_cpu_resume，其中 T_cpu_resume ≈ 0.1-0.3ms（仅签名验证），总 P99 纯处理部分 < 0.5ms；若使用 0-RTT，首包传输可重叠，但存在重放攻击风险检查开销约 0.2ms。

## Corrected Claim

TLS 1.3 Session Resumption（Session ID 或 Ticket）的 P99 延迟 T_tls_resume_p99 ≈ 0.5 RTT + T_cpu_resume，其中 T_cpu_resume ≈ 0.1-0.3ms（仅签名验证），总 P99 纯处理部分 < 0.5ms；若使用 0-RTT，首包传输可重叠，但存在重放攻击风险检查开销约 0.2ms。

## Evidence

先验知识/题面给定，逻辑校验通过

## Search Query

TLS 1.3 session resumption 0-RTT latency milliseconds CPU overhead
