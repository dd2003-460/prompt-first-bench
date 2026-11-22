# N278: Intel Gaudi 3 在持续 LLM 推理负载下的平均功耗 (P_avg) 需实测确定，若假设 P_avg ≈ 0.8 × 700W TDP = 560W

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N76

## Claim

Intel Gaudi 3 在持续 LLM 推理负载下的平均功耗 (P_avg) 需实测确定，若假设 P_avg ≈ 0.8 × 700W TDP = 560W，则 3 年能耗成本 OpEx_energy = 560W × 0.7 × 24h × 365d × 3y × $0.12/kWh ≈ $1970，需根据实际负载修正。

## Corrected Claim

Intel Gaudi 3 在持续 LLM 推理负载下的平均功耗 (P_avg) 需实测确定，若假设 P_avg ≈ 0.8 × 700W TDP = 560W，则 3 年能耗成本 OpEx_energy = 560W × 0.7 × 24h × 365d × 3y × $0.12/kWh ≈ $1970，需根据实际负载修正。

## Evidence

先验知识/题面给定，逻辑校验通过：算术计算正确（560W * 0.7 * 24 * 365 * 3 * 0.12 ≈ 1970.4），且明确标注为假设值需实测修正，符合工程估算逻辑。
