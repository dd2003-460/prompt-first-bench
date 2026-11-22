# N267: 分层抽样偏差校正项 δ_sampling：若分层抽样未覆盖长尾卖家（占比 < 5%），则 E[σ_noise_i] 会被低估，导致 δ_heterogeneit

- **status**: degraded
- **level**: L4
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 1
- **parent_ids**: N90

## Claim

分层抽样偏差校正项 δ_sampling：若分层抽样未覆盖长尾卖家（占比 < 5%），则 E[σ_noise_i] 会被低估，导致 δ_heterogeneity 高估；校正公式为 δ_corrected = δ_raw * (1 + (n_tail/n_total) * (σ_tail/σ_main - 1))，其中 σ_tail 为长尾卖家噪声标准差。

## Corrected Claim

分层抽样若未覆盖长尾卖家，可能导致噪声估计偏差进而影响异质性估计。具体的校正公式 δ_corrected = δ_raw * (1 + (n_tail/n_total) * (σ_tail/σ_main - 1)) 为特定模型下的近似表达，需结合具体统计模型验证其适用性。

## Evidence

[质询]校正公式 δ_corrected = δ_raw * (1 + (n_tail/n_total) * (σ_tail/σ_main - 1)) 在统计学上缺乏严谨推导支持。通常分层抽样偏差校正涉及方差估计的加权调整（如 Cochran 公式），而非简单的线性乘数校正。该公式假设噪声标准差与异质性偏差之间存在特定的线性比例关系，这在一般统计理论中并不成立，属于经验性或特定模型下的近似，而非通用事实。 | 先验知识/题面给定，逻辑校验通过（量纲一致，方向合理），但具体校正公式为经验性近似，缺乏通用统计理论直接支持，且无外部来源验证。

## Search Query

stratified sampling bias correction for variance estimation in long-tail distributions
