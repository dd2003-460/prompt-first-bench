# N366: 理论命中率 H 的数值解：代入 $N=12.3 \times 10^6$ 和 $K=7 \times 10^5$（假设 1TB 缓存），$H \approx \

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N136

## Claim

理论命中率 H 的数值解：代入 $N=12.3 \times 10^6$ 和 $K=7 \times 10^5$（假设 1TB 缓存），$H \approx \frac{\ln(7 \times 10^5)}{\ln(1.23 \times 10^7)} \approx \frac{13.46}{16.33} \approx 82.4\%$；此值用于后续 P99 延迟加权计算。

## Corrected Claim

理论命中率 H 的数值解：代入 $N=12.3 \times 10^6$ 和 $K=7 \times 10^5$（假设 1TB 缓存），$H \approx \frac{\ln(7 \times 10^5)}{\ln(1.23 \times 10^7)} \approx \frac{13.46}{16.33} \approx 82.4\%$；此值用于后续 P99 延迟加权计算。

## Evidence

先验知识/题面给定，逻辑校验通过：ln(7e5)≈13.46, ln(1.23e7)≈16.33, 比值≈0.824，计算无误。
