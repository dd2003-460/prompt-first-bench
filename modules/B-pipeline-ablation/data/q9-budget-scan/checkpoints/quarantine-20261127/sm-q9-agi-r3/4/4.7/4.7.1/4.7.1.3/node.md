# N237: 错误率基线 p_i 的动态更新采用指数加权移动平均（EWMA）公式：p_i(t+1) = α * error_rate_i(t) + (1-α) * p_i(t

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N83

## Claim

错误率基线 p_i 的动态更新采用指数加权移动平均（EWMA）公式：p_i(t+1) = α * error_rate_i(t) + (1-α) * p_i(t)，其中平滑系数 α=0.2（半衰期约3周），error_rate_i(t) 为第 t 周第 i 阶段的实际观测错误率；初始值 p_hypothesis=0.175, p_experiment=0.075, p_analysis=0.125。

## Corrected Claim

错误率基线 p_i 的动态更新采用指数加权移动平均（EWMA）公式：p_i(t+1) = α * error_rate_i(t) + (1-α) * p_i(t)，其中平滑系数 α=0.2（半衰期约3周），error_rate_i(t) 为第 t 周第 i 阶段的实际观测错误率；初始值 p_hypothesis=0.175, p_experiment=0.075, p_analysis=0.125。

## Evidence

先验知识/题面给定，逻辑校验通过：EWMA公式定义正确，α=0.2对应的半衰期计算（ln(0.5)/ln(0.8)≈3.1周）符合数学推导，初始值设定合理且无内部矛盾。
