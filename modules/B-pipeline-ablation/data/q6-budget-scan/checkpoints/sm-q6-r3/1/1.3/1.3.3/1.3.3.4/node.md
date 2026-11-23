# N128: P99 传输延迟 L_trans_p99 = s_p99 / Effective_Bandwidth_per_req，其中 Effective_Bandwidt

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N47

## Claim

P99 传输延迟 L_trans_p99 = s_p99 / Effective_Bandwidth_per_req，其中 Effective_Bandwidth_per_req = Peak_BW_per_POP / Concurrent_Requests_per_POP，若每 POP 并发请求数为 10,000，峰值带宽 1 Gbps，则单请求有效带宽 ≈ 100 Kbps = 12.5 KB/s

## Corrected Claim

P99 传输延迟 L_trans_p99 = s_p99 / Effective_Bandwidth_per_req，其中 Effective_Bandwidth_per_req = Peak_BW_per_POP / Concurrent_Requests_per_POP，若每 POP 并发请求数为 10,000，峰值带宽 1 Gbps，则单请求有效带宽 ≈ 100 Kbps = 12.5 KB/s

## Evidence

先验知识/题面给定，逻辑校验通过：1 Gbps / 10,000 = 100 Kbps，且 100 Kbps / 8 = 12.5 KB/s，数值换算准确，符合带宽均分的基本逻辑。
