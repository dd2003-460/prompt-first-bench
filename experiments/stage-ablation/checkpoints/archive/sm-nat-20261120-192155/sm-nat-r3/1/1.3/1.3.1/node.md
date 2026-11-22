# N27: 联合分布参数化：r_i = R_max * i^{-0.9}，s_i = S_max * i^{-1.1} * exp(-0.3 * (ln(i) - E[ln

- **status**: pending
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N7

## Claim

联合分布参数化：r_i = R_max * i^{-0.9}，s_i = S_max * i^{-1.1} * exp(-0.3 * (ln(i) - E[ln(i)]))，其中R_max = 5000万/天 / (Σ_{i=1}^{100000} i^{-0.9})，S_max为最大对象大小（需假设或从分布推导）

## Corrected Claim

联合分布参数化：r_i = R_max * i^{-0.9}，s_i = S_max * i^{-1.1} * exp(-0.3 * (ln(i) - E[ln(i)]))，其中R_max = 5000万/天 / (Σ_{i=1}^{100000} i^{-0.9})，S_max为最大对象大小（需假设或从分布推导）

## Evidence

父节点级核验未通过：非正交, 不完备（子节点2和3存在逻辑依赖和重复推导，非严格正交；且子节点1中关于R_max的数值计算存在严重数学错误（将求和近似为积分上限/指数，导致数量级错误），未正确覆盖父节点中S_max的推导/假设这一关键方面。）
