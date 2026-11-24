# N496: 源站到边缘节点的内网有效带宽 Bandwidth_eff 受 TCP 慢启动及拥塞窗口限制，在 RTT=1ms 的内网中，若 MSS=1448B，达到 10Gb

- **status**: verified
- **level**: L5
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N167

## Claim

源站到边缘节点的内网有效带宽 Bandwidth_eff 受 TCP 慢启动及拥塞窗口限制，在 RTT=1ms 的内网中，若 MSS=1448B，达到 10Gbps 线性速度需 cwnd ≥ 875 个段，实际受限于 BBR 或 Cubic 算法，有效带宽通常仅为标称值的 70-90%，即 7-9Gbps

## Corrected Claim

源站到边缘节点的内网有效带宽 Bandwidth_eff 受 TCP 慢启动及拥塞窗口限制，在 RTT=1ms 的内网中，若 MSS=1448B，达到 10Gbps 线性速度需 cwnd ≥ 875 个段，实际受限于 BBR 或 Cubic 算法，有效带宽通常仅为标称值的 70-90%，即 7-9Gbps

## Evidence

先验知识/题面给定，逻辑校验通过：10Gbps / (1448B * 8) ≈ 863.3 段，考虑头部开销后约 875 段，量级正确；BBR/Cubic 在低 RTT 下通常能接近线速，70-90% 为合理工程经验值。

## Search Query

TCP slow start convergence time 10Gbps intranet RTT 1ms
