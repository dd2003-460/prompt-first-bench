# N394: 骨干网带宽成本增量 ΔC_backhaul = C_backhaul_base * (1 - H_new) / (1 - H_base)，其中 C_backha

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N130, N131, N132

## Claim

骨干网带宽成本增量 ΔC_backhaul = C_backhaul_base * (1 - H_new) / (1 - H_base)，其中 C_backhaul_base 为基准回源带宽成本；当 H 从 90% 降至 72% 时，ΔC_backhaul = C_backhaul_base * (0.28/0.10) = 2.8 * C_backhaul_base，即骨干网成本增加 180%；若 C_backhaul_base = ¥50,000/月，则 ΔC_backhaul = ¥140,000/月。

## Corrected Claim

骨干网带宽成本增量 ΔC_backhaul = C_backhaul_base * (1 - H_new) / (1 - H_base)，其中 C_backhaul_base 为基准回源带宽成本；当 H 从 90% 降至 72% 时，ΔC_backhaul = C_backhaul_base * (0.28/0.10) = 2.8 * C_backhaul_base，即骨干网成本增加 180%；若 C_backhaul_base = ¥50,000/月，则 ΔC_backhaul = ¥140,000/月。

## Evidence

先验知识/题面给定，逻辑校验通过：公式推导正确，数值计算（0.28/0.10=2.8，增量180%，绝对值140,000）均准确无误。

## Search Query

CDN backhaul bandwidth cost cache hit rate
