# N227: 推导 H_byte_LRU_lower 的保守下界：H_byte_LRU_lower ≥ H_byte_Optimal - ε_lru - δ_ρ，其中 δ_ρ

- **status**: degraded
- **level**: L4
- **source**: search
- **edge_type**: quotient
- **rework_count**: 1
- **parent_ids**: N84

## Claim

推导 H_byte_LRU_lower 的保守下界：H_byte_LRU_lower ≥ H_byte_Optimal - ε_lru - δ_ρ，其中 δ_ρ 是负相关 ρ=-0.3 导致的额外损失（因为 LRU 驱逐策略未考虑大小，可能驱逐了高频小对象而保留低频大对象，加剧了字节命中率下降）。δ_ρ 可通过模拟 LRU 在双变量 Pareto 分布下的驱逐序列计算。

## Corrected Claim

H_byte_LRU_lower 的保守下界可表示为 H_byte_Optimal 减去 LRU 策略损失项 ε_lru 及由负相关系数 ρ 引起的额外损失 δ_ρ；其中 δ_ρ 的具体数值需通过模拟 LRU 在特定分布下的驱逐序列计算，而非固定为 ρ=-0.3 的单一结论。

## Evidence

[质询]该陈述包含具体的经验参数（ρ=-0.3）和特定的推导结论（δ_ρ 的具体来源及计算方式），属于经验事实/模型假设，无法仅从第一性原理严格推出，且缺乏外部来源支持其具体数值和逻辑链条的普适性。 | 经验事实，逻辑自洽但缺来源支持（本轮检索无可用来源）。

## Search Query

LRU byte hit rate loss size popularity correlation negative rho simulation
