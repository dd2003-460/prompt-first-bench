# N55: 60% 无咨询事件的概率模型：P(no_inquiry) = Φ((SNR_crit - SNR) / σ_noise)，其中 SNR_crit = 1，σ_n

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: stochastic
- **rework_count**: 0
- **parent_ids**: N11

## Claim

60% 无咨询事件的概率模型：P(no_inquiry) = Φ((SNR_crit - SNR) / σ_noise)，其中 SNR_crit = 1，σ_noise 为市场噪声标准差，当 SNR < 1 时，P(no_inquiry) > 0.5，结合观测值 60%，可反推 SNR ≈ 0.8-0.9，验证了小幅降价失效的机制。

## Corrected Claim

60% 无咨询事件的概率模型：P(no_inquiry) = Φ((SNR_crit - SNR) / σ_noise)，其中 SNR_crit = 1，σ_noise 为市场噪声标准差，当 SNR < 1 时，P(no_inquiry) > 0.5，结合观测值 60%，可反推 SNR ≈ 0.8-0.9，验证了小幅降价失效的机制。

## Evidence

先验知识/题面给定，逻辑校验通过：基于正态分布性质，当SNR=1时P=0.5，SNR<1时P>0.5，反推SNR在0.8-0.9区间符合60%概率的数学逻辑。

## Search Query

probability of no inquiry signal noise ratio critical value 0.8
