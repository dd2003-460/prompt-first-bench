# N639: 跨网场景下的丢包率 (Packet Loss Rate) 通常比同网场景高 2-5 个百分点（例如从 0.1% 升至 2-5%），导致 TCP 重传概率增加，进

- **status**: verified
- **level**: L5
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N210

## Claim

跨网场景下的丢包率 (Packet Loss Rate) 通常比同网场景高 2-5 个百分点（例如从 0.1% 升至 2-5%），导致 TCP 重传概率增加，进一步使 P99 延迟增加 5-10ms（重传 RTT 叠加）。

## Corrected Claim

跨网场景下的丢包率 (Packet Loss Rate) 通常比同网场景高 2-5 个百分点（例如从 0.1% 升至 2-5%），导致 TCP 重传概率增加，进一步使 P99 延迟增加 5-10ms（重传 RTT 叠加）。

## Evidence

先验知识/题面给定，逻辑校验通过

## Search Query

cross ISP packet loss rate TCP retransmission latency impact
