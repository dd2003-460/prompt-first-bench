# N237: 基线投诉率 R_base 的置信区间：R_base = 0.5% - 1.5%，标准误 SE_R = sqrt(R_base*(1-R_base)/n_user

- **status**: degraded
- **level**: L4
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 1
- **parent_ids**: N78

## Claim

基线投诉率 R_base 的置信区间：R_base = 0.5% - 1.5%，标准误 SE_R = sqrt(R_base*(1-R_base)/n_users)。若 n_users = 100,000，SE_R ≈ 0.002%，R_base 的 95% CI 为 [0.496%, 1.504%]。

## Corrected Claim

若 n_users = 100,000，当 R_base = 0.5% 时，SE_R ≈ 0.007%，95% CI 约为 [0.486%, 0.514%]；当 R_base = 1.5% 时，SE_R ≈ 0.012%，95% CI 约为 [1.476%, 1.524%]。

## Evidence

[质询]数值量级严重错误：当 n_users=100,000 且 R_base 在 0.5%-1.5% 之间时，标准误 SE_R 应在 0.007% 到 0.011% 之间，而非 0.002%；且 95% 置信区间 [0.496%, 1.504%] 的宽度（约 1.008%）与基于该标准误计算出的理论宽度（约 0.028%-0.043%）相差两个数量级，内部逻辑矛盾。 | 逻辑校验失败：根据二项分布标准误公式 SE = sqrt(p(1-p)/n)，代入 p=0.005, n=100000 计算得 SE≈0.00007 (即 0.007%)，与陈述中的 0.002% 不符；且 95% CI 应为点估计 ± 1.96*SE，陈述中的区间宽度远大于理论值，存在硬逻辑错误。

## Search Query

baseline complaint rate e-commerce platform confidence interval
