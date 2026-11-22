# N74: 归因置信度上限的重新计算：基于修正后的 $\epsilon_w \approx 0.158$，黑箱下的置信度上限为 $1 - 0.158 = 0.842$。若平

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N22

## Claim

归因置信度上限的重新计算：基于修正后的 $\epsilon_w \approx 0.158$，黑箱下的置信度上限为 $1 - 0.158 = 0.842$。若平台公开算法，$\epsilon_{model}$ 降至 0.02，$\epsilon_w \approx \sqrt{0.02^2 + 0.05^2} \approx 0.054$，置信度上限升至 $1 - 0.054 = 0.946$。这证实了 N22 中 0.8 和 0.95 的估计基本合理，但需明确误差来源。

## Corrected Claim

归因置信度上限的重新计算：基于修正后的 $\epsilon_w \approx 0.158$，黑箱下的置信度上限为 $1 - 0.158 = 0.842$。若平台公开算法，$\epsilon_{model}$ 降至 0.02，$\epsilon_w \approx \sqrt{0.02^2 + 0.05^2} \approx 0.054$，置信度上限升至 $1 - 0.054 = 0.946$。这证实了 N22 中 0.8 和 0.95 的估计基本合理，但需明确误差来源。

## Evidence

先验知识/题面给定，逻辑校验通过：算术运算正确（1-0.158=0.842, sqrt(0.0004+0.0025)≈0.054, 1-0.054=0.946），且结论与N22的估计值（0.8, 0.95）在合理误差范围内一致，逻辑自洽。

## Search Query

confidence interval for algorithmic attribution in platform economics
