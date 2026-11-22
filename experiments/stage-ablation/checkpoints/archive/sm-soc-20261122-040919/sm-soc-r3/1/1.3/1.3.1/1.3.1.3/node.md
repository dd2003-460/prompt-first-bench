# N153: 信号噪声对搜索成本降低系数 k 的耦合影响：k_effective = k_base * (1 - α * σ²_signal)。其中 k_base=0.6 为

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: stochastic
- **rework_count**: 0
- **parent_ids**: N38

## Claim

信号噪声对搜索成本降低系数 k 的耦合影响：k_effective = k_base * (1 - α * σ²_signal)。其中 k_base=0.6 为无噪声时的基准值，α 为噪声敏感度系数（假设 α=1.0 为线性近似）。若 σ²_signal=0.1（即标准差 0.316），则 k_effective = 0.6 * (1 - 0.1) = 0.54。这表明信号噪声每增加 10% 的方差，k 值下降约 10%，直接削弱买家对‘快速成交’信号的依赖。

## Corrected Claim

信号噪声对搜索成本降低系数 k 的耦合影响：k_effective = k_base * (1 - α * σ²_signal)。其中 k_base=0.6 为无噪声时的基准值，α 为噪声敏感度系数（假设 α=1.0 为线性近似）。若 σ²_signal=0.1（即标准差 0.316），则 k_effective = 0.6 * (1 - 0.1) = 0.54。这表明信号噪声每增加 10% 的方差，k 值下降约 10%，直接削弱买家对‘快速成交’信号的依赖。

## Evidence

先验知识/题面给定，逻辑校验通过

## Search Query

signal noise impact on search cost reduction coefficient
