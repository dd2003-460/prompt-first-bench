# N13: LFU 增益上限工作点 2（中性价比最优）：考虑更新率 1%/天，LFU 需老化机制（aging），有效频率 R'_k = R_k * exp(-λ t)，λ 

- **status**: degraded
- **level**: L2
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 1
- **parent_ids**: N1, N2, N3

## Claim

LFU 增益上限工作点 2（中性价比最优）：考虑更新率 1%/天，LFU 需老化机制（aging），有效频率 R'_k = R_k * exp(-λ t)，λ 由更新率决定；此时 LFU 增益 Δ_opt ≈ Δ_max * exp(-λ T_c)，其中 T_c 是平均驻留时间，Δ_opt 比 Δ_max 低 20-40% [待核验]

## Corrected Claim

LFU 增益上限工作点 2（中性价比最优）：考虑更新率 1%/天，LFU 需老化机制（aging），有效频率 R'_k = R_k * exp(-λ t)，λ 由更新率决定；此时 LFU 增益 Δ_opt ≈ Δ_max * exp(-λ T_c)，其中 T_c 是平均驻留时间，Δ_opt 通常低于 Δ_max，具体降幅取决于负载特征与参数配置。

## Evidence

[质询]该陈述包含具体的经验性数值范围（20-40%）和特定的数学模型形式（指数衰减），这些并非LFU算法的通用第一性原理推论，而是依赖于特定负载分布和参数设定的经验结论，缺乏通用性。 | 先验知识/题面给定，逻辑校验通过：LFU引入老化机制（Aging）以解决频率过时问题，其增益确实会因老化系数λ和驻留时间Tc的乘积而衰减，逻辑自洽；但具体数值范围（20-40%）属于经验事实，无来源支持，故降级。

## Search Query

LFU aging mechanism cache update rate
