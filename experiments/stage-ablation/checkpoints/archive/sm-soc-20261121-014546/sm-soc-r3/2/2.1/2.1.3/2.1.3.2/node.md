# N194: 下游投影 1：60% 无咨询概率的反推，P(no_inquiry) = Φ((1 - SNR) / σ_noise) = 0.6，解得 (1 - SNR) / 

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: stochastic
- **rework_count**: 0
- **parent_ids**: N55

## Claim

下游投影 1：60% 无咨询概率的反推，P(no_inquiry) = Φ((1 - SNR) / σ_noise) = 0.6，解得 (1 - SNR) / σ_noise = Φ^{-1}(0.6) ≈ 0.253，若 σ_noise = 0.1，则 SNR ≈ 0.975，验证了小幅降价失效。

## Corrected Claim

下游投影 1：60% 无咨询概率的反推，P(no_inquiry) = Φ((1 - SNR) / σ_noise) = 0.6，解得 (1 - SNR) / σ_noise = Φ^{-1}(0.6) ≈ 0.253，若 σ_noise = 0.1，则 SNR ≈ 0.975，验证了小幅降价失效。

## Evidence

先验知识/题面给定，逻辑校验通过：Φ(0.253)≈0.6，(1-SNR)/0.1=0.253 => SNR=0.9747≈0.975，数学推导自洽。

## Search Query

inverse normal distribution 60 percent no inquiry probability back calculation
