# N39: 搜索成本降低系数 k 的动态表达式：$k = 1 - \frac{C_{search}^{prior}}{C_{search}^{post}}$，其中 $C_{

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: stochastic
- **rework_count**: 0
- **parent_ids**: N7

## Claim

搜索成本降低系数 k 的动态表达式：$k = 1 - \frac{C_{search}^{prior}}{C_{search}^{post}}$，其中 $C_{search}^{prior}$ 为无信号时的预期搜索成本，$C_{search}^{post}$ 为有‘快速成交’信号后的预期搜索成本，k=0.6 意味着信号使搜索成本降低了60%，该值受信号噪声 $\sigma^2_{signal}$ 的负向影响。

## Corrected Claim

搜索成本降低系数 k 的动态表达式：$k = 1 - \frac{C_{search}^{prior}}{C_{search}^{post}}$，其中 $C_{search}^{prior}$ 为无信号时的预期搜索成本，$C_{search}^{post}$ 为有‘快速成交’信号后的预期搜索成本，k=0.6 意味着信号使搜索成本降低了60%，该值受信号噪声 $\sigma^2_{signal}$ 的负向影响。

## Evidence

先验知识/题面给定，逻辑校验通过：公式定义符合成本降低系数的数学逻辑，k=0.6对应60%降低在量级上自洽，信号噪声对成本的正向影响（即对降低系数的负向影响）符合信息经济学直觉。

## Search Query

dynamic expression for search cost reduction coefficient in signaling models
