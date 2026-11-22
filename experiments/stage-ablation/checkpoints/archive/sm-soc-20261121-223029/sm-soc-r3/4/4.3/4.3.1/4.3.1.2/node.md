# N250: 降价幅度 ΔP 对 48 小时咨询量恢复率 R_inquiry 的弹性系数 β：R_inquiry(k, ΔP) = R_base * (k^α) * (ΔP^

- **status**: degraded
- **level**: L4
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N83

## Claim

降价幅度 ΔP 对 48 小时咨询量恢复率 R_inquiry 的弹性系数 β：R_inquiry(k, ΔP) = R_base * (k^α) * (ΔP^β)，其中 β ∈ [0.8, 1.5]，需通过 A/B 测试数据估计 β 的具体数值。

## Corrected Claim

降价幅度 ΔP 对 48 小时咨询量恢复率 R_inquiry 的弹性系数 β 需通过 A/B 测试数据估计，其具体数值和函数形式（如 R_inquiry(k, ΔP) = R_base * (k^α) * (ΔP^β)）应基于实证数据确定，而非预设固定范围。

## Evidence

[质询]该陈述包含具体的经验参数范围（β ∈ [0.8, 1.5]）和特定的函数形式，属于经验事实。在缺乏任何外部来源支持的情况下，无法验证该弹性系数的具体数值范围是否准确，也无法排除其他可能的函数形式或参数区间。 | 经验事实，逻辑自洽但缺来源支持（本轮检索无可用来源）

## Search Query

price reduction magnitude delta P effect on inquiry recovery rate beta elasticity
