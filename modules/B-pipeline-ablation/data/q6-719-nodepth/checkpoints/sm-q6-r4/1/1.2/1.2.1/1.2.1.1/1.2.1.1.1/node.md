# N456: 拥塞抖动 σ_congestion 的临界阈值 ρ_critical 推导：当 ρ → 1 时，σ_congestion → ∞，实际网络中 ρ > 0.9 时

- **status**: degraded
- **level**: L5
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 1
- **parent_ids**: N153

## Claim

拥塞抖动 σ_congestion 的临界阈值 ρ_critical 推导：当 ρ → 1 时，σ_congestion → ∞，实际网络中 ρ > 0.9 时抖动方差急剧增大；为确保 P99 延迟稳定，需控制 ρ ≤ 0.7，此时 σ_congestion ≈ σ_base × (1 / 0.3) ≈ 3.3 × σ_base，若 σ_base = 1.5ms，则 σ_congestion ≈ 5ms，P99 延迟增加约 3 × σ_congestion = 15ms。

## Corrected Claim

拥塞抖动 σ_congestion 随负载 ρ 增加而显著增大，当 ρ > 0.9 时方差急剧上升；工程上常建议控制 ρ ≤ 0.7 以维持 P99 延迟稳定，此时抖动约为基线的 3 倍左右（具体倍数取决于队列模型和流量特征）。

## Evidence

[质询]该陈述将复杂的网络排队论（如M/M/1模型）简化为线性比例关系（σ ≈ σ_base / (1-ρ)），忽略了排队延迟通常与方差（σ²）或更高阶矩相关，且P99延迟增加量并非简单的3σ线性叠加，属于过度简化的经验近似而非严格推导。 | 先验知识/题面给定，逻辑校验通过（量级合理，符合排队论中负载接近1时延迟急剧上升的定性规律，但具体数值系数为经验近似）
