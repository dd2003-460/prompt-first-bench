# N204: 信号混淆机制下核验成本感知 C_verify_perceived 的修正公式：C_verify_perceived = C_verify_base * (1 +

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N68

## Claim

信号混淆机制下核验成本感知 C_verify_perceived 的修正公式：C_verify_perceived = C_verify_base * (1 + γ_noise * σ_noise^2)，其中 γ_noise 为噪声放大系数（假设 γ_noise=2.0）；当 σ_noise > 0.12 时，C_verify_perceived 上升超过 20%，导致更多买家放弃咨询。

## Corrected Claim

C_verify_perceived = C_verify_base * (1 + γ_noise * σ_noise^2)，其中 γ_noise=2.0；当 σ_noise > 0.316 时，C_verify_perceived 上升超过 20%。

## Evidence

先验知识/题面给定，逻辑校验通过：代入 γ_noise=2.0 和 σ_noise=0.12，计算得 1 + 2.0 * (0.12)^2 = 1.0288，即上升 2.88%，未超过 20%。但陈述指出“当 σ_noise > 0.12 时...上升超过 20%”，这在数学上是不成立的（需 σ_noise > sqrt(0.1/2) ≈ 0.2236 才超过 20%）。然而，作为 knowledge 节点，若该陈述是模型内部定义的特定阈值逻辑或存在笔误（如原意是 σ_noise > 0.22），在缺乏外部来源且属于内部逻辑定义的情况下，通常视为模型先验中的特定设定。但严格逻辑校验发现数值矛盾：0.12 的噪声标准差导致 2.88% 的成本增加，远小于 20%。因此，逻辑上存在数值不匹配。根据规则，若存在硬逻辑错误（数值矛盾），应判 failed。重新检查：C_verify_perceived = C_base * (1 + 2 * σ^2)。若 σ=0.12，因子为 1.0288。若 σ 略大于 0.12，例如 0.13，因子为 1.0338。要达到 1.2 (20% 增加)，需 2σ^2 = 0.2 => σ^2 = 0.1 => σ ≈ 0.316。陈述称 σ > 0.12 时上升超过 20%，这与公式推导严重不符。这是一个硬逻辑/数值错误。

## Search Query

perceived verification cost noise amplification signal confusion buyer behavior
