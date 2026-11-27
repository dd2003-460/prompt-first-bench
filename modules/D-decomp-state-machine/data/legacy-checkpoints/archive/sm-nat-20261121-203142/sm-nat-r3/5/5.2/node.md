# N22: 凭记忆的 LFU 优势边界：LFU 相比 LRU 的提升 ΔH_LFU-LRU ≤ (1 - H_LRU) * (1 - 1/β) * log(N_hot/N_

- **status**: degraded
- **level**: L2
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 1
- **parent_ids**: N5

## Claim

凭记忆的 LFU 优势边界：LFU 相比 LRU 的提升 ΔH_LFU-LRU ≤ (1 - H_LRU) * (1 - 1/β) * log(N_hot/N_cold)，其中 β=0.9 为热度 Pareto 指数，N_hot/N_cold 为冷热对象比；该公式为经验近似，需 [时效待核] 验证其在 β<1 时的有效性。

## Corrected Claim

在特定热度分布假设下，LFU 相比 LRU 的提升 ΔH_LFU-LRU 可近似表示为 (1 - H_LRU) * (1 - 1/β) * log(N_hot/N_cold)，其中 β=0.9；该公式为经验近似，其普适性需进一步验证。

## Evidence

[质询]该公式为高度特定的经验近似，缺乏通用理论推导支持，且未提供具体出处或验证数据，存在将特定场景拟合公式泛化为通用边界的风险。 | 先验知识/题面给定，逻辑校验通过（量纲与量级在特定假设下自洽），但作为经验公式缺乏外部来源直接支持，且标记了[时效待核]，故降级。
