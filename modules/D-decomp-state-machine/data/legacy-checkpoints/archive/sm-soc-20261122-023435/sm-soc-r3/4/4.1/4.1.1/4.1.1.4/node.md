# N149: 噪声抵消项 η_noise 的量化：η_noise = σ_noise / (σ_noise + σ_signal)，其中 σ_noise 为展示数据的统计波动

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N49

## Claim

噪声抵消项 η_noise 的量化：η_noise = σ_noise / (σ_noise + σ_signal)，其中 σ_noise 为展示数据的统计波动标准差，σ_signal 为真实价格信号强度，当样本量 N_sample < 30 时，该噪声项显著增大，降低透明化效率。

## Corrected Claim

噪声抵消项 η_noise 的量化：η_noise = σ_noise / (σ_noise + σ_signal)，其中 σ_noise 为展示数据的统计波动标准差，σ_signal 为真实价格信号强度，当样本量 N_sample < 30 时，该噪声项显著增大，降低透明化效率。

## Evidence

先验知识/题面给定，逻辑校验通过
