# N133: 成交周期缩短效应量 ΔT 的置信区间构建：计算 ΔT 的 95% CI 为 [ΔT - 1.96*SE_ΔT, ΔT + 1.96*SE_ΔT]，其中 SE_Δ

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N49

## Claim

成交周期缩短效应量 ΔT 的置信区间构建：计算 ΔT 的 95% CI 为 [ΔT - 1.96*SE_ΔT, ΔT + 1.96*SE_ΔT]，其中 SE_ΔT 基于样本标准差和样本量 n 计算；若 CI 下界 > 0 且 ΔT > 0.5 * T_deal_baseline，则判定效应显著且具备实际意义。

## Corrected Claim

成交周期缩短效应量 ΔT 的置信区间构建：计算 ΔT 的 95% CI 为 [ΔT - 1.96*SE_ΔT, ΔT + 1.96*SE_ΔT]，其中 SE_ΔT 基于样本标准差和样本量 n 计算；若 CI 下界 > 0 且 ΔT > 0.5 * T_deal_baseline，则判定效应显著且具备实际意义。

## Evidence

先验知识/题面给定，逻辑校验通过

## Search Query

confidence interval calculation for difference in means transaction time
