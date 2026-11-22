# N310: 阈值 0.2 的统计显著性检验：检验 H0: (ΔExposure/Exposure_base) <= 0.2，需计算该比值的 95% 置信区间 [CI_low

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N103

## Claim

阈值 0.2 的统计显著性检验：检验 H0: (ΔExposure/Exposure_base) <= 0.2，需计算该比值的 95% 置信区间 [CI_lower, CI_upper]，若 CI_lower > 0.2 则拒绝 H0，支持平台驱动假设；若 CI_upper < 0.2 则支持卖家行为假设；置信度 Conf = P(|t| > t_crit | data)。

## Corrected Claim

阈值 0.2 的统计显著性检验：检验 H0: (ΔExposure/Exposure_base) <= 0.2，需计算该比值的 95% 置信区间 [CI_lower, CI_upper]，若 CI_lower > 0.2 则拒绝 H0，支持平台驱动假设；若 CI_upper < 0.2 则支持卖家行为假设；置信度 Conf = P(|t| > t_crit | data)。

## Evidence

先验知识/题面给定，逻辑校验通过
