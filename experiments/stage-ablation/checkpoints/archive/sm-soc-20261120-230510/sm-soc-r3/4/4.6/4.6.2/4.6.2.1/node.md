# N245: 在干预措施B下，截断正态分布 TruncatedNormal(μ=V, σ=σ, min=P_median*0.8, max=P_median*1.15) 下 

- **status**: degraded
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N81

## Claim

在干预措施B下，截断正态分布 TruncatedNormal(μ=V, σ=σ, min=P_median*0.8, max=P_median*1.15) 下 E[min(V_i)] 的解析近似公式：E[min(V_i)] ≈ μ - σ * (Φ^{-1}(1 - 1/N_choices) * (1 - Φ((max-μ)/σ) - Φ((min-μ)/σ)) / (Φ((max-μ)/σ) - Φ((min-μ)/σ)))，其中 N_choices 为剩余选择集大小，用于替代定性估计。

## Corrected Claim

在干预措施B下，若 V_i 服从截断正态分布 TruncatedNormal(μ=V, σ=σ, min=P_median*0.8, max=P_median*1.15)，则单个 V_i 的期望 E[V_i] 由截断正态分布的标准公式给出：E[V_i] = μ + σ * (φ((min-μ)/σ) - φ((max-μ)/σ)) / (Φ((max-μ)/σ) - Φ((min-μ)/σ))。若需计算 N_choices 个独立同分布变量中的最小值期望 E[min(V_1, ..., V_N)]，需通过数值积分或模拟计算，无简单解析近似公式。

## Evidence

[质询]公式结构存在严重逻辑错误：截断正态分布的期望值 E[X] 仅取决于分布参数 (μ, σ, min, max)，与样本量 N_choices 无关。该公式试图将分位数逆函数 Φ^{-1}(1 - 1/N_choices) 与截断概率区间比值相乘并减去，这在数学上无意义，混淆了'从N个独立样本中取最小值的期望'与'单个截断正态变量的期望'，且量纲和逻辑均不自洽。 | 逻辑校验失败：截断正态分布的期望是分布固有属性，不随 N_choices 变化；公式中引入 N_choices 的项缺乏统计学依据，属于硬逻辑错误。
