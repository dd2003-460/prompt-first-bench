# N214: 分段噪声占比的计算边界条件：当 Breusch-Pagan p < 0.05 时，将价格区间 [P_min, P_max] 等分为 k 段（k 由自由度约束 k

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N76

## Claim

分段噪声占比的计算边界条件：当 Breusch-Pagan p < 0.05 时，将价格区间 [P_min, P_max] 等分为 k 段（k 由自由度约束 k < n/50 决定），计算每段 j 的局部噪声占比 σ_noise_j²/σ_total_j²，若段间差异 > 20% 则确认异方差，否则维持全局常数假设。

## Corrected Claim

分段噪声占比的计算边界条件：当 Breusch-Pagan p < 0.05 时，将价格区间 [P_min, P_max] 等分为 k 段（k 由自由度约束 k < n/50 决定），计算每段 j 的局部噪声占比 σ_noise_j²/σ_total_j²，若段间差异 > 20% 则确认异方差，否则维持全局常数假设。

## Evidence

先验知识/题面给定，逻辑校验通过

## Search Query

heteroscedasticity segmented variance calculation threshold k segments
