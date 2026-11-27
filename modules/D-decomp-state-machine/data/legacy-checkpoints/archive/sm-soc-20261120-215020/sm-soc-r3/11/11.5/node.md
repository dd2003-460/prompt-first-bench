# N242: 似然比 LR=4.67 的统计显著性检验：LR 本身不是 p 值，需转换为对数似然比（Deviance）进行卡方检验。Deviance = 2 * ln(LR)

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N84

## Claim

似然比 LR=4.67 的统计显著性检验：LR 本身不是 p 值，需转换为对数似然比（Deviance）进行卡方检验。Deviance = 2 * ln(LR) = 2 * ln(4.67) ≈ 3.10。自由度 df=1（两个假设，一个参数差异）。在 df=1 时，卡方临界值 3.84 对应 p=0.05。由于 3.10 < 3.84，p > 0.05，说明在 95% 置信水平下，H_signal 并不显著优于 H0。需增加样本量或放宽置信水平至 90%（临界值 2.71，此时 p < 0.10）才能支持 H_signal。

## Corrected Claim

似然比 LR=4.67 的统计显著性检验：LR 本身不是 p 值，需转换为对数似然比（Deviance）进行卡方检验。Deviance = 2 * ln(LR) = 2 * ln(4.67) ≈ 3.10。自由度 df=1（两个假设，一个参数差异）。在 df=1 时，卡方临界值 3.84 对应 p=0.05。由于 3.10 < 3.84，p > 0.05，说明在 95% 置信水平下，H_signal 并不显著优于 H0。需增加样本量或放宽置信水平至 90%（临界值 2.71，此时 p < 0.10）才能支持 H_signal。

## Evidence

先验知识/题面给定，逻辑校验通过：LR=4.67转换为Deviance=2*ln(4.67)≈3.10，df=1时卡方临界值3.84对应p=0.05，3.10<3.84故p>0.05，结论正确

## Search Query

likelihood ratio test chi-square critical value statistical significance
