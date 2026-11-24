# N737: 中带宽配置下的排队延迟增量 ΔT_queue 计算：基于 M/M/1 模型，ΔT_queue = (ρ / (μ(1-ρ)))，其中 ρ = λ/μ，需确保 Δ

- **status**: verified
- **level**: L5
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N253

## Claim

中带宽配置下的排队延迟增量 ΔT_queue 计算：基于 M/M/1 模型，ΔT_queue = (ρ / (μ(1-ρ)))，其中 ρ = λ/μ，需确保 ΔT_queue < 5ms 以满足 P99 约束，若 ρ > 0.8 则需增加服务器或带宽

## Corrected Claim

中带宽配置下的排队延迟增量 ΔT_queue 计算：基于 M/M/1 模型，ΔT_queue = (ρ / (μ(1-ρ)))，其中 ρ = λ/μ，需确保 ΔT_queue < 5ms 以满足 P99 约束，若 ρ > 0.8 则需增加服务器或带宽

## Evidence

先验知识/题面给定，逻辑校验通过：M/M/1排队模型中平均等待时间公式 Wq = ρ/(μ(1-ρ)) 正确，且 ρ>0.8 时延迟急剧增加需扩容符合排队论基本直觉
