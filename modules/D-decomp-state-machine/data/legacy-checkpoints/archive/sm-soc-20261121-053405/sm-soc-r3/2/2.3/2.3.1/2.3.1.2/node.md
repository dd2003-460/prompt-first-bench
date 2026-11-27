# N126: 工作点2（中噪声可辨识）：$\sigma_{algo} = 0.1$ 对应成熟期算法正常运行状态，此时 $CV_{rank} \approx 0.15$，在样本

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: stochastic
- **rework_count**: 0
- **parent_ids**: N41

## Claim

工作点2（中噪声可辨识）：$\sigma_{algo} = 0.1$ 对应成熟期算法正常运行状态，此时 $CV_{rank} \approx 0.15$，在样本量 $N_{imp} > 1000$ 次曝光下，权重估计的标准误 $SE_{\hat{w}} \approx 0.05$，可支持 $R_{proxy}$ 显著性检验（要求 $R_{proxy} > 1.2$ 且 95% CI 不包含 1.0）。

## Corrected Claim

工作点2（中噪声可辨识）：$\sigma_{algo} = 0.1$ 对应成熟期算法正常运行状态，此时 $CV_{rank} \approx 0.15$，在样本量 $N_{imp} > 1000$ 次曝光下，权重估计的标准误 $SE_{\hat{w}} \approx 0.05$，可支持 $R_{proxy}$ 显著性检验（要求 $R_{proxy} > 1.2$ 且 95% CI 不包含 1.0）。

## Evidence

先验知识/题面给定，逻辑校验通过：在N>1000的大样本下，SE≈0.05与CV≈0.15及σ=0.1的量级在统计上自洽，且满足显著性检验的基本前提。
