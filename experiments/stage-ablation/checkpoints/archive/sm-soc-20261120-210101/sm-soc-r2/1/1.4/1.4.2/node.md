# N43: 信号过滤机制的参数化：P_match(ΔP) = P_base * exp(- (ΔP - μ_signal)^2 / 2σ_pref^2) 中，μ_signa

- **status**: degraded
- **level**: L3
- **source**: search
- **edge_type**: stochastic
- **rework_count**: 1
- **parent_ids**: N9, N10, N11

## Claim

信号过滤机制的参数化：P_match(ΔP) = P_base * exp(- (ΔP - μ_signal)^2 / 2σ_pref^2) 中，μ_signal 并非市场均价，而是‘高信用卖家’的加权均价。具体地，μ_signal = Σ(w_i * P_i)，其中 w_i 为卖家 i 的信用分归一化权重。若高信用卖家占比 H_credit > 0.6，则 μ_signal 向上偏移 δ_offset，导致 ΔP ∈ [15%, 25%] 区间落在高匹配概率的‘峰顶’附近，而非‘尾部’。

## Corrected Claim

在特定的信号过滤机制模型中，若定义 μ_signal 为高信用卖家的加权均价，且高信用卖家占比超过特定阈值（如 0.6），则可能导致匹配概率峰值向特定价格区间偏移。

## Evidence

[质询]该陈述包含具体的经验性阈值（H_credit > 0.6）和特定的参数化公式，属于特定模型或场景下的经验事实，无法从第一性原理严格推导，且缺乏来源支持其具体数值和逻辑关系的普适性。 | 经验事实，逻辑自洽但缺来源支持

## Search Query

signal filtering effect in second-hand market pricing
