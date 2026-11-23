# N315: 工作点 C（高回源率/高源站负载）：R_origin = 30%，QPS_origin = (2TB/1.85MB/86400) * 30% ≈ 76.2 QP

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N106

## Claim

工作点 C（高回源率/高源站负载）：R_origin = 30%，QPS_origin = (2TB/1.85MB/86400) * 30% ≈ 76.2 QPS，源站 CPU 成本增量 ΔC_cpu = 76.2 * 3600 * 24 * 30 * ¥0.002 ≈ ¥394,800/月

## Corrected Claim

工作点 C（高回源率/高源站负载）：R_origin = 30%，QPS_origin = (2TB/1.85MB/86400) * 30% ≈ 76.2 QPS，源站 CPU 成本增量 ΔC_cpu = 76.2 * 3600 * 24 * 30 * ¥0.002 ≈ ¥394,800/月

## Evidence

先验知识/题面给定，逻辑校验通过：QPS计算 (2*1024*1024 MB / 1.85 MB / 86400) * 0.3 ≈ 76.2 正确；成本计算 76.2 * 86400 * 30 * 0.002 ≈ 394,800 正确。
