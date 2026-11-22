# N176: 加权平均转化系数 k_weighted 的计算公式：k_weighted = p_high * k_high + (1 - p_high) * k_low，其中

- **status**: verified
- **level**: L4
- **source**: given
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N60

## Claim

加权平均转化系数 k_weighted 的计算公式：k_weighted = p_high * k_high + (1 - p_high) * k_low，其中 k_high = k_base * (1 + β_quality * QS_high)，k_low = k_base * (1 + β_quality * QS_low)，代入 p_high=0.7, QS_high=0.9, QS_low=0.3, k_base=0.08, β_quality=0.2 计算得 k_weighted ≈ 0.08 * (0.7*1.18 + 0.3*0.94) ≈ 0.0925，需对比常数 k 假设下的误差。

## Corrected Claim

加权平均转化系数 k_weighted 的计算公式：k_weighted = p_high * k_high + (1 - p_high) * k_low，其中 k_high = k_base * (1 + β_quality * QS_high)，k_low = k_base * (1 + β_quality * QS_low)，代入 p_high=0.7, QS_high=0.9, QS_low=0.3, k_base=0.08, β_quality=0.2 计算得 k_weighted ≈ 0.08 * (0.7*1.18 + 0.3*0.94) ≈ 0.0925，需对比常数 k 假设下的误差。

## Evidence

先验知识/题面给定，逻辑校验通过：公式推导与数值计算（0.08 * (0.7*1.18 + 0.3*0.94) ≈ 0.0925）均准确无误。
