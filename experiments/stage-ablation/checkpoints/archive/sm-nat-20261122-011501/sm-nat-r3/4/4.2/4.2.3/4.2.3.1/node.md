# N130: T_res_weighted 的解析近似：在 Pareto(α=1.1) 大小分布和 Pareto(β=0.9) 热度分布独立假设下，T_res_weighte

- **status**: degraded
- **level**: L4
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 1
- **parent_ids**: N54

## Claim

T_res_weighted 的解析近似：在 Pareto(α=1.1) 大小分布和 Pareto(β=0.9) 热度分布独立假设下，T_res_weighted ≈ E[S] * E[1/H] / E[1/H|S]。由于 ρ=-0.3，小对象（高频）权重高，导致 T_res_weighted 显著高于几何平均驻留时间，预计比算术平均 T_res 高 15-25%。

## Corrected Claim

在 Pareto(α=1.1) 大小分布和 Pareto(β=0.9) 热度分布独立假设下，由于负相关（ρ=-0.3）导致小对象（高频）权重较高，T_res_weighted 预计显著高于几何平均驻留时间，且通常高于算术平均 T_res，但具体高出比例（如15-25%）需依赖具体参数模拟验证，不宜作为通用解析结论。

## Evidence

[质询]公式 T_res_weighted ≈ E[S] * E[1/H] / E[1/H|S] 在数学上缺乏严谨推导支持，且将加权平均驻留时间与算术平均/几何平均的相对关系（高15-25%）直接关联到特定的相关系数 ρ=-0.3 存在逻辑跳跃，该具体百分比区间缺乏通用理论保证，可能因具体分布参数或定义口径不同而大幅波动。 | 先验知识/题面给定，逻辑校验通过（量纲一致，方向性符合直觉：高频小对象权重高会拉高加权平均），但具体数值区间（15-25%）及特定解析近似公式的普适性无法仅凭逻辑自洽完全确证，且无外部来源支持，故降级。
