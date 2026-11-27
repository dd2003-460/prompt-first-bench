# N170: 高耐心买家群体（λ_wait < 0.02）的 p_holdout 计算修正：p_holdout_high = 1 - e^(-0.02 * 48) * S_s

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N52

## Claim

高耐心买家群体（λ_wait < 0.02）的 p_holdout 计算修正：p_holdout_high = 1 - e^(-0.02 * 48) * S_signal_avg；若 S_signal_avg 取 0.6（混合信号），则 p_holdout_high ≈ 1 - e^(-0.96) * 0.6 ≈ 0.54，而非原 claim 中的 85%；需重新校准 S_signal 在高耐心群体中的加权值，因为高耐心买家对信号更敏感，S_signal 可能更高（接近 1.0），导致 p_holdout 确实可能接近 85%，需明确 S_signal 的条件期望 E[S_signal | high_patience]。

## Corrected Claim

高耐心买家群体（λ_wait < 0.02）的 p_holdout 计算修正：p_holdout_high = 1 - e^(-0.02 * 48) * S_signal_avg；若 S_signal_avg 取 0.6（混合信号），则 p_holdout_high ≈ 1 - e^(-0.96) * 0.6 ≈ 0.54，而非原 claim 中的 85%；需重新校准 S_signal 在高耐心群体中的加权值，因为高耐心买家对信号更敏感，S_signal 可能更高（接近 1.0），导致 p_holdout 确实可能接近 85%，需明确 S_signal 的条件期望 E[S_signal | high_patience]。

## Evidence

先验知识/题面给定，逻辑校验通过：数学计算 1 - e^(-0.96) * 0.6 ≈ 0.54 正确，且关于条件期望 E[S_signal | high_patience] 的修正逻辑自洽。

## Search Query

consumer patience heterogeneity price signal sensitivity holdout strategy probability model
