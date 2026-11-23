# N181: 回源流量到达率 $\lambda$ 基于回源比例 $(1-H)$ 计算：$\lambda = (R_{daily} \times (1-H)) / 86400$

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N61

## Claim

回源流量到达率 $\lambda$ 基于回源比例 $(1-H)$ 计算：$\lambda = (R_{daily} \times (1-H)) / 86400$，假设 $R_{daily}=2,000,000$ req/day 且 $H=90\%$，则 $\lambda \approx 2.31$ req/s；该值是计算排队延迟 $L_{queue}$ 的关键输入。

## Corrected Claim

回源流量到达率 $\lambda$ 基于回源比例 $(1-H)$ 计算：$\lambda = (R_{daily} \times (1-H)) / 86400$，假设 $R_{daily}=2,000,000$ req/day 且 $H=90\%$，则 $\lambda \approx 2.31$ req/s；该值是计算排队延迟 $L_{queue}$ 的关键输入。

## Evidence

先验知识/题面给定，逻辑校验通过：计算过程 2,000,000 * 0.1 / 86400 ≈ 2.3148，数值量级与公式逻辑自洽。
