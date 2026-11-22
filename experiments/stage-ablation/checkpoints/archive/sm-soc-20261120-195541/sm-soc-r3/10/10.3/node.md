# N205: 60% 无咨询现象的归因分解：计算噪声单独贡献的无咨询比例 P_no_consult_noise = 1 - exp(-σ_noise^2 / σ_crit^2

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N68

## Claim

60% 无咨询现象的归因分解：计算噪声单独贡献的无咨询比例 P_no_consult_noise = 1 - exp(-σ_noise^2 / σ_crit^2) 和信号混淆单独贡献的比例 P_no_consult_confusion = 1 - exp(-γ_noise * σ_noise^2)；若两者之和 < 60%，则需引入交互项修正，表明单一机制不足。

## Corrected Claim

60% 无咨询现象的归因分解：计算噪声单独贡献的无咨询比例 P_no_consult_noise = 1 - exp(-σ_noise^2 / σ_crit^2) 和信号混淆单独贡献的比例 P_no_consult_confusion = 1 - exp(-γ_noise * σ_noise^2)；若两者之和 < 60%，则需引入交互项修正，表明单一机制不足。

## Evidence

先验知识/题面给定，逻辑校验通过

## Search Query

attribution decomposition no consultation rate noise signal confusion interaction effect
