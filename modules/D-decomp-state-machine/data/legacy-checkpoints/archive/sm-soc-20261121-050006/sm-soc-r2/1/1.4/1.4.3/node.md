# N46: 新咨询率 ΔQ 的具体函数形式：ΔQ = -κ_signal * (ΔU / σ_pref) + η_traffic，其中 κ_signal 为信号敏感度系数（

- **status**: degraded
- **level**: L3
- **source**: knowledge
- **edge_type**: stochastic
- **rework_count**: 1
- **parent_ids**: N8

## Claim

新咨询率 ΔQ 的具体函数形式：ΔQ = -κ_signal * (ΔU / σ_pref) + η_traffic，其中 κ_signal 为信号敏感度系数（实证估计值约为 0.8-1.2），η_traffic 为平台自然流量噪声（均值为0，方差 σ²_traffic）；当 ΔU 超过 0.5σ_pref 时，-κ_signal * 0.5 项主导，导致 ΔQ 显著为负，解释 60% 无咨询现象。

## Corrected Claim

新咨询率 ΔQ 可建模为 ΔQ = -κ_signal * (ΔU / σ_pref) + η_traffic，其中 κ_signal 为信号敏感度系数，η_traffic 为平台自然流量噪声。当 ΔU 显著为正时，负向信号项主导，导致 ΔQ 为负，从而解释部分无咨询现象。

## Evidence

[质询]该陈述包含具体的实证估计值（κ_signal 约为 0.8-1.2）和具体的现象解释比例（解释 60% 无咨询现象），这些属于经验事实。虽然 source 标记为 knowledge，但缺乏外部来源支持，且“解释 60%”这一具体数值缺乏推导依据，存在过度精确化的风险。 | 逻辑结构自洽（线性模型+噪声），但具体系数范围和解释比例属于经验参数，无来源直接支持，依据经验事实排除条款降级。
