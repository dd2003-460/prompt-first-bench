# N80: Markov 链稳态概率的具体状态定义：状态空间为 {Fresh, Stale}，转移概率矩阵为 [[1-u, u], [0, 1]]（假设更新后对象立即变为 

- **status**: pending
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N22, N23

## Claim

Markov 链稳态概率的具体状态定义：状态空间为 {Fresh, Stale}，转移概率矩阵为 [[1-u, u], [0, 1]]（假设更新后对象立即变为 Stale 且不再命中），稳态概率 π_Stale = u / (u + (1-u)/T_avg_resident) 的修正形式。

## Corrected Claim

Markov 链稳态概率的具体状态定义：状态空间为 {Fresh, Stale}，转移概率矩阵为 [[1-u, u], [0, 1]]。若 T_avg_resident 定义为平均驻留步数（无量纲），则稳态概率 π_Stale = u / (u + (1-u)/T_avg_resident) 成立；否则需修正量纲。

## Evidence

父节点级核验失败（LLM 错误）：Unterminated string starting at: line 9 column 5 (char 804)
