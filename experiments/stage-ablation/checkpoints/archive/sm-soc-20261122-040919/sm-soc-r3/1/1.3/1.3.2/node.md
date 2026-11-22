# N39: 搜索成本降低系数 k 的动态表达式：$k = 1 - \frac{C_{search}^{prior}}{C_{search}^{post}}$，其中 $C_{

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N7

## Claim

搜索成本降低系数 k 的动态表达式：$k = 1 - \frac{C_{search}^{prior}}{C_{search}^{post}}$，其中 $C_{search}^{prior}$ 为无信号时的预期搜索成本，$C_{search}^{post}$ 为有‘快速成交’信号后的预期搜索成本，k=0.6 意味着信号使搜索成本降低了60%，该值受信号噪声 $\sigma^2_{signal}$ 的负向影响。

## Corrected Claim

搜索成本降低系数 k 的动态表达式：$k = 1 - \frac{C_{search}^{prior}}{C_{search}^{post}}$，其中 $C_{search}^{prior}$ 为无信号时的预期搜索成本，$C_{search}^{post}$ 为有‘快速成交’信号后的预期搜索成本，k=0.6 意味着信号使搜索成本降低了60%，该值受信号噪声 $\sigma^2_{signal}$ 的负向影响。

## Evidence

父节点级核验通过：正交+完备+无冗余（子节点覆盖了误差源、先验成本分解、后验成本分解与一致性校准、以及敏感性分析四个维度，彼此独立且互补，无重复或矛盾。）

## Search Query

dynamic expression for search cost reduction coefficient in signaling models
