# N105: 策略转换阈值 θ_hold 的动态校准：θ_hold 并非固定 5%，而是随卖家现金流紧张度 C_urgency 动态变化，模型为 θ_hold = θ_bas

- **status**: degraded
- **level**: L3
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N30, N31, N32

## Claim

策略转换阈值 θ_hold 的动态校准：θ_hold 并非固定 5%，而是随卖家现金流紧张度 C_urgency 动态变化，模型为 θ_hold = θ_base × (1 + γ_urgency × C_urgency)，其中 θ_base=3%，γ_urgency=0.5。当卖家月均收入低于中位数 50% 时，C_urgency=1，θ_hold 升至 4.5%；当卖家为职业卖家时，C_urgency=0，θ_hold 降至 3%。

## Corrected Claim

策略转换阈值 θ_hold 的动态校准：θ_hold 随卖家现金流紧张度 C_urgency 动态变化，模型为 θ_hold = θ_base × (1 + γ_urgency × C_urgency)。具体参数值（如 θ_base, γ_urgency）及 C_urgency 的定义需依据具体模型设定或实证数据确定。

## Evidence

[质询]该陈述包含具体的经验参数（θ_base=3%, γ_urgency=0.5）及特定的业务逻辑定义（C_urgency的触发条件），属于经验事实而非第一性原理可推导内容，且缺乏外部来源支持。 | 经验事实，逻辑自洽但缺来源支持

## Search Query

dynamic threshold seller cash flow urgency holding cost strategy switch empirical data
