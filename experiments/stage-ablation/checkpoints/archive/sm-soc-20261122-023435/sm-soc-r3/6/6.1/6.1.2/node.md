# N214: ΔCTR 的置信区间与样本量关系：当 N < 5 时，ΔCTR 的 95% 置信区间为 [μ_ΔCTR - 1.96*σ_ΔCTR/sqrt(n), μ_ΔCT

- **status**: degraded
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N68

## Claim

ΔCTR 的置信区间与样本量关系：当 N < 5 时，ΔCTR 的 95% 置信区间为 [μ_ΔCTR - 1.96*σ_ΔCTR/sqrt(n), μ_ΔCTR + 1.96*σ_ΔCTR/sqrt(n)]，若样本量 n < 30，则置信区间宽度超过 ±10%，使得 18% 的提升在统计上不显著，需增加样本量或采用贝叶斯先验修正。

## Corrected Claim

ΔCTR 的 95% 置信区间公式为 [μ_ΔCTR - 1.96*σ_ΔCTR/sqrt(n), μ_ΔCTR + 1.96*σ_ΔCTR/sqrt(n)]。当样本量 n 较小时（如 n < 30），置信区间通常较宽，可能导致中等幅度（如 18%）的提升在统计上不显著，具体显著性取决于基线 CTR 和方差，需增加样本量或采用贝叶斯先验修正。

## Evidence

[质询]陈述中关于“样本量 n < 30 时置信区间宽度超过 ±10%”以及“18% 的提升在统计上不显著”的具体数值结论缺乏前提条件（如基线 CTR 值、方差大小），属于经验性断言而非普适统计规律；不同基线 CTR 下，n<30 的置信区间宽度差异巨大，该具体阈值不具备通用逻辑必然性。 | 先验知识/题面给定，逻辑校验通过：置信区间公式正确，但具体数值结论（±10%、18%不显著）依赖于未给出的基线参数，属于特定场景下的经验推断，缺乏通用性，故降级。

## Search Query

statistical significance small sample size click through rate lift confidence interval
