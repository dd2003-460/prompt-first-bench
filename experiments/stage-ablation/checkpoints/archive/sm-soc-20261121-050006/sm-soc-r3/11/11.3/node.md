# N353: 阈值 σ²_pref_ess 的敏感性分析：当 C_info 变动 ±20% 或 V_match 变动 ±20% 时，σ²_pref_ess 的变动幅度及对应匹

- **status**: degraded
- **level**: L4
- **source**: search
- **edge_type**: quotient
- **rework_count**: 1
- **parent_ids**: N114

## Claim

阈值 σ²_pref_ess 的敏感性分析：当 C_info 变动 ±20% 或 V_match 变动 ±20% 时，σ²_pref_ess 的变动幅度及对应匹配失败率 P(fail) = 1 - Φ(√(V_match/(2*C_info))) 的变化范围，用于确定该阈值在实证数据中的鲁棒性区间。

## Corrected Claim

阈值 σ²_pref_ess 的敏感性分析框架：通过调整 C_info 和 V_match ±20%，利用公式 P(fail) = 1 - Φ(√(V_match/(2*C_info))) 计算匹配失败率的变化，以评估阈值在实证数据中的鲁棒性。具体变动幅度需基于实际基准参数计算。

## Evidence

[质询]该陈述描述的是一个具体的敏感性分析结果（即变动幅度及变化范围），属于经验事实或特定模型计算结果，而非通用的数学恒等式或第一性原理可直接推出的固定数值。由于缺乏具体的模型参数（如 C_info 和 V_match 的基准值），无法从第一性原理推导出确切的“变动幅度”和“变化范围”，且检索无可用来源支持这一具体结论。 | 经验事实，逻辑自洽但缺来源支持。公式 P(fail) = 1 - Φ(√(V_match/(2*C_info))) 在逻辑上成立，但具体的敏感性分析结果（±20% 变动对应的具体范围）依赖于未提供的基准参数，且无外部来源验证。

## Search Query

sensitivity analysis ESS threshold variance preference noise matching failure rate C2C market
