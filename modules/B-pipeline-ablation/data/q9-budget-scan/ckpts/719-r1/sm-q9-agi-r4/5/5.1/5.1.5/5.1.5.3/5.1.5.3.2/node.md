# N663: 重试策略成本模型：采用指数退避重试（最多 3 次），重试概率 P_retry = 1 - (1-λ_fail)^k，其中 k=3，P_retry ≈ 0.003

- **status**: verified
- **level**: L5
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N242

## Claim

重试策略成本模型：采用指数退避重试（最多 3 次），重试概率 P_retry = 1 - (1-λ_fail)^k，其中 k=3，P_retry ≈ 0.003；每次重试消耗 100% 原始 Token，额外成本 Cost_extra = Cost_per_call * P_retry * N_calls = $0.035 * 0.003 * 100 = $0.0105/天

## Corrected Claim

重试策略成本模型：采用指数退避重试（最多 3 次），重试概率 P_retry = 1 - (1-λ_fail)^k，其中 k=3，P_retry ≈ 0.003；每次重试消耗 100% 原始 Token，额外成本 Cost_extra = Cost_per_call * P_retry * N_calls = $0.035 * 0.003 * 100 = $0.0105/天

## Evidence

先验知识/题面给定，逻辑校验通过：数学计算正确（0.035*0.003*100=0.0105），指数退避重试成本模型符合常规工程假设，数值量级合理。
