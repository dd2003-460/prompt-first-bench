# N58: TLS握手延迟 T_handshake：对于新建TCP+TLS连接，完整握手需要2-3个RTT，每次RTT贡献 T_handshake_per_rtt ≈ 20

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N9

## Claim

TLS握手延迟 T_handshake：对于新建TCP+TLS连接，完整握手需要2-3个RTT，每次RTT贡献 T_handshake_per_rtt ≈ 20-50ms（取决于RTT），总握手延迟 P99 约为 40-150ms；若使用HTTP/2或HTTP/3复用连接，可避免握手延迟，P99 < 5ms。

## Corrected Claim

TLS握手延迟 T_handshake：对于新建TCP+TLS连接，完整握手需要2-3个RTT，每次RTT贡献 T_handshake_per_rtt ≈ 20-50ms（取决于RTT），总握手延迟 P99 约为 40-150ms；若使用HTTP/2或HTTP/3复用连接，可避免握手延迟，P99 < 5ms。

## Evidence

父节点级核验通过：正交+完备+无冗余（子节点分别对应父节点中提到的不同技术场景（TLS 1.2, TLS 1.3, QUIC/HTTP 3, 连接复用），覆盖了父节点描述的所有关键方面（2-3 RTT 的具体拆解、HTTP/2/3 复用避免握手）。各子节点定义明确，无重复或矛盾。）
