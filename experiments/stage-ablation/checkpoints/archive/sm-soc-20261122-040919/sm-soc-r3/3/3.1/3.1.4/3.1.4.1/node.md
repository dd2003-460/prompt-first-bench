# N249: 共享随机源：点击率 CTR 的波动源。CTR_new 受价格透明度影响，其方差 Var(CTR) 取决于用户群体异质性。假设 CTR ~ Beta(α, β)，

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: stochastic
- **rework_count**: 0
- **parent_ids**: N68

## Claim

共享随机源：点击率 CTR 的波动源。CTR_new 受价格透明度影响，其方差 Var(CTR) 取决于用户群体异质性。假设 CTR ~ Beta(α, β)，需估计 α 和 β 以确定 CTR 的置信区间，进而影响算法调整幅度。

## Corrected Claim

共享随机源：点击率 CTR 的波动源。CTR_new 受价格透明度影响，其方差 Var(CTR) 取决于用户群体异质性。假设 CTR ~ Beta(α, β)，需估计 α 和 β 以确定 CTR 的置信区间，进而影响算法调整幅度。

## Evidence

先验知识/题面给定，逻辑校验通过：Beta分布常用于建模[0,1]区间内的比率数据（如CTR），其方差公式 Var = αβ/((α+β)^2(α+β+1)) 确实依赖于参数α和β，且用户异质性通常通过增加分布的离散度（即改变α, β）来体现，逻辑自洽。
