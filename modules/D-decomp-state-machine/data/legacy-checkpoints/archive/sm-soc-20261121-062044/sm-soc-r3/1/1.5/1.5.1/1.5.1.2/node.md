# N124: 惰性阈值均值 μ_s 的估计方法：基于点击率 (CTR) 数据，构建逻辑回归模型 logit(P(click)) = α + β * Δp + ε，μ_s 对应

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N39

## Claim

惰性阈值均值 μ_s 的估计方法：基于点击率 (CTR) 数据，构建逻辑回归模型 logit(P(click)) = α + β * Δp + ε，μ_s 对应于 P(click) = 0.5 时的 Δp 值，即 μ_s = -α/β，需控制商品类目和位置偏差。

## Corrected Claim

惰性阈值均值 μ_s 的估计方法：基于点击率 (CTR) 数据，构建逻辑回归模型 logit(P(click)) = α + β * Δp + ε，μ_s 对应于 P(click) = 0.5 时的 Δp 值，即 μ_s = -α/β，需控制商品类目和位置偏差。

## Evidence

先验知识/题面给定，逻辑校验通过：逻辑回归中 P=0.5 对应 logit=0，即 α+βΔp=0，解得 Δp=-α/β，数学推导自洽且符合统计学常识。
