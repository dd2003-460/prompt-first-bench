# N391: 联合扰动下的带宽成本增量公式 ΔC_bw = C_bw_base * [ (1 + Δs) * (1 - H_new) / (1 - H_base) - 1 ]

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N130, N131, N132

## Claim

联合扰动下的带宽成本增量公式 ΔC_bw = C_bw_base * [ (1 + Δs) * (1 - H_new) / (1 - H_base) - 1 ]，其中 Δs = 0.2，H_new 由 N137 模型计算；代入数值：若 H_base=85%, H_new=83.8%，则 ΔC_bw ≈ C_bw_base * [1.2 * (0.162/0.15) - 1] = C_bw_base * [1.2 * 1.08 - 1] = C_bw_base * 0.296，即成本增加 29.6%，弹性系数 E_bw = 0.296/0.2 = 1.48 > 1。

## Corrected Claim

联合扰动下的带宽成本增量公式 ΔC_bw = C_bw_base * [ (1 + Δs) * (1 - H_new) / (1 - H_base) - 1 ]，其中 Δs = 0.2，H_new 由 N137 模型计算；代入数值：若 H_base=85%, H_new=83.8%，则 ΔC_bw ≈ C_bw_base * [1.2 * (0.162/0.15) - 1] = C_bw_base * [1.2 * 1.08 - 1] = C_bw_base * 0.296，即成本增加 29.6%，弹性系数 E_bw = 0.296/0.2 = 1.48 > 1。

## Evidence

先验知识/题面给定，逻辑校验通过：公式推导符合代数逻辑，数值计算（1.2 * 1.08 - 1 = 0.296）准确，弹性系数定义（增量/扰动）合理。

## Search Query

CDN bandwidth cost sensitivity object size cache hit rate
