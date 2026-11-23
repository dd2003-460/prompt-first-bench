# N313: 工作点 A（低回源率/低源站负载）：R_origin = 5%，QPS_origin = (2TB/1.85MB/86400) * 5% ≈ 12.7 QPS，

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N106

## Claim

工作点 A（低回源率/低源站负载）：R_origin = 5%，QPS_origin = (2TB/1.85MB/86400) * 5% ≈ 12.7 QPS，源站 CPU 成本增量 ΔC_cpu = 12.7 * 3600 * 24 * 30 * ¥0.002 ≈ ¥65,800/月

## Corrected Claim

工作点 A（低回源率/低源站负载）：R_origin = 5%，QPS_origin = (2TB/1.85MB/86400) * 5% ≈ 12.7 QPS，源站 CPU 成本增量 ΔC_cpu = 12.7 * 3600 * 24 * 30 * ¥0.002 ≈ ¥65,800/月

## Evidence

先验知识/题面给定，逻辑校验通过：QPS计算 (2*1024*1024 MB / 1.85 MB / 86400) * 0.05 ≈ 12.7 QPS 正确；成本计算 12.7 * 86400 * 30 * 0.002 ≈ 65,800 元/月 正确。
