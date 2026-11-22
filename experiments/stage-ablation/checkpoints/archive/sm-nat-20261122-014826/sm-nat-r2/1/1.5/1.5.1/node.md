# N36: ρ=-0.3 对有效容量利用率的精确量化：定义偏差因子 δ = (E[s | in_CLRU] - E[s | in_Coptimal]) / E[s | in

- **status**: degraded
- **level**: L3
- **source**: search
- **edge_type**: quotient
- **rework_count**: 1
- **parent_ids**: N10

## Claim

ρ=-0.3 对有效容量利用率的精确量化：定义偏差因子 δ = (E[s | in_CLRU] - E[s | in_Coptimal]) / E[s | in_Coptimal]。基于负相关系数，δ ≈ -0.12（即 LRU 保留的对象平均比最优小 12%），导致有效容量 C_eff = 128GB * (1/0.88) ≈ 145GB。

## Corrected Claim

基于负相关系数 ρ=-0.3，推测 LRU 保留对象平均尺寸略小于最优策略，导致有效容量利用率下降，具体量化值（如 δ≈-0.12, C_eff≈145GB）需依赖具体负载分布假设，此处仅为估算。

## Evidence

[质询]从相关系数 ρ=-0.3 直接推导偏差因子 δ ≈ -0.12 缺乏统计学依据（相关系数不等于均值偏差比例，且未提供分布假设），属于经验事实的强行量化，逻辑链条存在跳跃。 | 经验事实，逻辑自洽但缺来源支持（检索无可用来源，且 ρ 到 δ 的转换非第一性原理可严格推导）

## Search Query

impact of negative correlation between object size and popularity on LRU cache effective capacity
