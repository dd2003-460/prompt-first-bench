# N58: ΔEff 的完整公式修正：ΔEff = (1 + ΔV/V) * (1 / (1 + ΔT/T)) - 1。原公式假设 ΔV=0 且 ΔT=-10%。若引入 N

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N19

## Claim

ΔEff 的完整公式修正：ΔEff = (1 + ΔV/V) * (1 / (1 + ΔT/T)) - 1。原公式假设 ΔV=0 且 ΔT=-10%。若引入 N30 的 ΔV 和 N31 的加权 ΔT，则 ΔEff 的预测值需重新计算，例如若 ΔV=0, ΔT_weighted=-2%，则 ΔEff ≈ 2.04%，远低于 21%。

## Corrected Claim

ΔEff 的完整公式修正：ΔEff = (1 + ΔV/V) * (1 / (1 + ΔT/T)) - 1。原公式假设 ΔV=0 且 ΔT=-10%。若引入 N30 的 ΔV 和 N31 的加权 ΔT，则 ΔEff 的预测值需重新计算，例如若 ΔV=0, ΔT_weighted=-2%，则 ΔEff ≈ 2.04%，远低于 21%。

## Evidence

先验知识/题面给定，逻辑校验通过：公式推导符合代数逻辑，数值计算 (1/0.98 - 1 ≈ 2.04%) 准确，且明确标注为示例场景。
