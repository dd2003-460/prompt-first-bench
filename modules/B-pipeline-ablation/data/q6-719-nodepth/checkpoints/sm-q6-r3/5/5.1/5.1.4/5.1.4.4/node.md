# N274: 流量调度与 DNS 解析额外延迟 L_switching_overhead 的量化：DNS 解析平均 20-50ms（首次），但 CDN 调度通常结合 Anyc

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N90

## Claim

流量调度与 DNS 解析额外延迟 L_switching_overhead 的量化：DNS 解析平均 20-50ms（首次），但 CDN 调度通常结合 Anycast 或智能 DNS，实际增量延迟主要为路由收敛和连接建立，L_switching_overhead ≈ 2-5ms；若采用 HTTP/3 或 QUIC，连接建立延迟可忽略，取 5ms 作为保守上限。

## Corrected Claim

流量调度与 DNS 解析额外延迟 L_switching_overhead 的量化：DNS 解析平均 20-50ms（首次），但 CDN 调度通常结合 Anycast 或智能 DNS，实际增量延迟主要为路由收敛和连接建立，L_switching_overhead ≈ 2-5ms；若采用 HTTP/3 或 QUIC，连接建立延迟可忽略，取 5ms 作为保守上限。

## Evidence

先验知识/题面给定，逻辑校验通过
