# N223: ESS 成立的临界 $w_{rel}^{*}$ 满足 $\Delta \Pi = 0$。解方程 $(1.2-0.5) \times 0.8 + w_{rel}^

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N77

## Claim

ESS 成立的临界 $w_{rel}^{*}$ 满足 $\Delta \Pi = 0$。解方程 $(1.2-0.5) \times 0.8 + w_{rel}^{*} \log(1.2) = (0.9-0.5) \times 1.2 + w_{rel}^{*} \log(0.9)$，得 $w_{rel}^{*} = \frac{0.56 - 0.48}{\log(1.2) - \log(0.9)} \approx \frac{0.08}{0.299} \approx 0.268$。即当 $w_{rel} < 0.268$ 时，低价策略占优；当 $w_{rel} > 0.268$ 时，高挂价为 ESS。

## Corrected Claim

ESS 成立的临界 $w_{rel}^{*}$ 满足 $\Delta \Pi = 0$。解方程 $(1.2-0.5) \times 0.8 + w_{rel}^{*} \log(1.2) = (0.9-0.5) \times 1.2 + w_{rel}^{*} \log(0.9)$，得 $w_{rel}^{*} = \frac{0.56 - 0.48}{\log(1.2) - \log(0.9)} \approx \frac{0.08}{0.299} \approx 0.268$。即当 $w_{rel} < 0.268$ 时，低价策略占优；当 $w_{rel} > 0.268$ 时，高挂价为 ESS。

## Evidence

先验知识/题面给定，逻辑校验通过：方程构建符合ESS临界条件定义，数值计算（0.08/0.299≈0.268）准确，量纲与逻辑自洽。
