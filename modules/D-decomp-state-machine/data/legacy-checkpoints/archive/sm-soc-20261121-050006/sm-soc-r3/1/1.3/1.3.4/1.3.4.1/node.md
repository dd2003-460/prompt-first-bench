# N148: 阈值 P_threshold 的量化公式：P_threshold = P_median * (1 + k_ess * σ_pref / P_median)，其中

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N43

## Claim

阈值 P_threshold 的量化公式：P_threshold = P_median * (1 + k_ess * σ_pref / P_median)，其中 k_ess 为演化稳定策略下的噪声容忍系数，估计值为 1.5-2.0；当 P_ask > P_threshold 时，匹配概率 p_match 降至 0.05 以下，T_close 超过 30 天（视为无穷大）

## Corrected Claim

阈值 P_threshold 的量化公式：P_threshold = P_median * (1 + k_ess * σ_pref / P_median)，其中 k_ess 为演化稳定策略下的噪声容忍系数，估计值为 1.5-2.0；当 P_ask > P_threshold 时，匹配概率 p_match 降至 0.05 以下，T_close 超过 30 天（视为无穷大）

## Evidence

先验知识/题面给定，逻辑校验通过

## Search Query

evolutionary stable strategy threshold price preference noise matching probability cutoff
