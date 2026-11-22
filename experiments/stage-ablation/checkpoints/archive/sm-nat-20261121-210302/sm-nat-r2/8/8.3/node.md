# N80: Markov 链稳态概率的具体状态定义：状态空间为 {Fresh, Stale}，转移概率矩阵为 [[1-u, u], [0, 1]]（假设更新后对象立即变为 

- **status**: degraded
- **level**: L3
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 1
- **parent_ids**: N22, N23

## Claim

Markov 链稳态概率的具体状态定义：状态空间为 {Fresh, Stale}，转移概率矩阵为 [[1-u, u], [0, 1]]（假设更新后对象立即变为 Stale 且不再命中），稳态概率 π_Stale = u / (u + (1-u)/T_avg_resident) 的修正形式。

## Corrected Claim

Markov 链稳态概率的具体状态定义：状态空间为 {Fresh, Stale}，转移概率矩阵为 [[1-u, u], [0, 1]]。若 T_avg_resident 定义为平均驻留步数（无量纲），则稳态概率 π_Stale = u / (u + (1-u)/T_avg_resident) 成立；否则需修正量纲。

## Evidence

[质询]稳态概率公式中的分母项 (1-u)/T_avg_resident 量纲存疑：若 T_avg_resident 是时间单位，则 (1-u)/T 具有频率量纲，与无量纲的 u 相加在数学上不自洽；若 T 是平均驻留步数（无量纲），则公式逻辑成立，但陈述中未明确 T 的定义，且 '假设更新后对象立即变为 Stale 且不再命中' 与矩阵第二行 [0, 1]（Stale 状态自环概率为 1，即永远 Stale）存在语义上的细微冲突（通常 '不再命中' 意味着进入吸收态或移除，而矩阵显示 Stale 状态持续存在）。 | 先验知识/题面给定，逻辑校验发现量纲或状态定义存在歧义，无法确认为 verified。
