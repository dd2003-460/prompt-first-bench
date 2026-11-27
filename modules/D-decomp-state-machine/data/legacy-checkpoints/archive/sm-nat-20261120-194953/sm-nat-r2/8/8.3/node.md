# N76: Pareto(α=1.1, S_min=1KB, S_max=100MB)分布的均值 $E[S] = \frac{\alpha S_{min}}{\alpha-

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N25

## Claim

Pareto(α=1.1, S_min=1KB, S_max=100MB)分布的均值 $E[S] = \frac{\alpha S_{min}}{\alpha-1}(1 - (S_{min}/S_{max})^{\alpha-1}) \approx \frac{1.1 \times 1}{0.1}(1 - (1/100000)^{0.1}) \approx 11 \times (1 - 0.063) \approx 10.3$ KB，而非1MB

## Corrected Claim

Pareto(α=1.1, S_min=1KB, S_max=100MB)分布的均值 $E[S] = \frac{\alpha S_{min}}{\alpha-1}(1 - (S_{min}/S_{max})^{\alpha-1}) \approx \frac{1.1 \times 1}{0.1}(1 - (1/100000)^{0.1}) \approx 11 \times (1 - 0.063) \approx 10.3$ KB，而非1MB

## Evidence

先验知识/题面给定，逻辑校验通过：截断Pareto分布均值公式正确，数值计算 (1/100000)^0.1 ≈ 0.0631，11*(1-0.0631) ≈ 10.3 KB，量级与逻辑均自洽。
