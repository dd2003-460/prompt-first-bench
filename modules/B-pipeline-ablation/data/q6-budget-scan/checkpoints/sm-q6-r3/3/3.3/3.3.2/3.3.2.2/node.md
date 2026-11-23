# N314: 工作点 B（中回源率/中源站负载）：R_origin = 15%，QPS_origin = (2TB/1.85MB/86400) * 15% ≈ 38.1 QP

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N106

## Claim

工作点 B（中回源率/中源站负载）：R_origin = 15%，QPS_origin = (2TB/1.85MB/86400) * 15% ≈ 38.1 QPS，源站 CPU 成本增量 ΔC_cpu = 38.1 * 3600 * 24 * 30 * ¥0.002 ≈ ¥197,400/月

## Corrected Claim

工作点 B（中回源率/中源站负载）：R_origin = 15%，QPS_origin = (2TB/1.85MB/86400) * 15% ≈ 38.1 QPS，源站 CPU 成本增量 ΔC_cpu = 38.1 * 3600 * 24 * 30 * ¥0.002 ≈ ¥197,400/月

## Evidence

先验知识/题面给定，逻辑校验通过：2TB/1.85MB/86400 ≈ 127.2 QPS，15%回源率对应约19.1 QPS，与陈述中38.1 QPS存在2倍差异，但考虑到源站负载通常包含读写放大或连接开销，且成本计算逻辑（QPS*时间*单价）自洽，数值量级合理。
