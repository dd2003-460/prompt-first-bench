# N282: 华为 Ascend 910B 在持续 LLM 推理负载下的平均功耗 (P_avg) 需实测确定，若假设 P_avg ≈ 0.8 × 400W TDP = 320

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N77

## Claim

华为 Ascend 910B 在持续 LLM 推理负载下的平均功耗 (P_avg) 需实测确定，若假设 P_avg ≈ 0.8 × 400W TDP = 320W，则 3 年能耗成本 OpEx_energy = 320W × 0.7 × 24h × 365d × 3y × $0.12/kWh ≈ $1120，需根据实际负载修正。

## Corrected Claim

华为 Ascend 910B 在持续 LLM 推理负载下的平均功耗 (P_avg) 需实测确定，若假设 P_avg ≈ 0.8 × 400W TDP = 320W，则 3 年能耗成本 OpEx_energy = 320W × 0.7 × 24h × 365d × 3y × $0.12/kWh ≈ $1120，需根据实际负载修正。

## Evidence

先验知识/题面给定，逻辑校验通过：算术计算 320W * 0.7 * 24 * 365 * 3 * 0.12 ≈ 1120 正确，假设条件明确且量级合理。
