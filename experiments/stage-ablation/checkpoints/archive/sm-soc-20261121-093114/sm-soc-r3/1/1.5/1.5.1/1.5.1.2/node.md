# N123: 下游投影 2：注意力衰减对咨询到达率 λ_consult 的影响量化为 λ_consult(t) = λ_base * A(t)，其中 λ_base 为基线咨询

- **status**: degraded
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N40

## Claim

下游投影 2：注意力衰减对咨询到达率 λ_consult 的影响量化为 λ_consult(t) = λ_base * A(t)，其中 λ_base 为基线咨询率，需验证 λ_consult(48h) 是否显著低于 λ_base，以确认注意力衰减是 60% 无咨询现象的主因。

## Corrected Claim

注意力衰减对咨询到达率有显著负面影响，可建模为 λ_consult(t) ≈ λ_base * A(t) * f(other_factors)，需通过控制变量实验验证其是否为60%无咨询现象的主因。

## Evidence

[质询]该陈述将复杂的用户行为（咨询到达率）简化为单一变量（注意力衰减）的线性乘积模型，忽略了价格、产品匹配度、用户意图等其他关键混杂因素，存在将相关当因果及模型过度简化的风险。 | source=knowledge，逻辑上公式定义自洽且量纲合理，但作为经验事实的量化模型，缺乏外部来源直接支持其作为'主因'的充分性，故降级。
