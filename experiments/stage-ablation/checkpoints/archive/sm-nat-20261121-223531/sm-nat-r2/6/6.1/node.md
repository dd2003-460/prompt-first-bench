# N70: Pareto分布截断均值 $E[S]_{trunc}$ 的精确计算公式为 $E[S]_{trunc} = \frac{\alpha-1}{\alpha-2} s

- **status**: degraded
- **level**: L3
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 1
- **parent_ids**: N22

## Claim

Pareto分布截断均值 $E[S]_{trunc}$ 的精确计算公式为 $E[S]_{trunc} = \frac{\alpha-1}{\alpha-2} s_{min} (1 - (s_{min}/s_{max})^{2-\alpha})$，当 $\alpha=1.1, s_{min}=1\text{KB}, s_{max}=100\text{MB}$ 时，计算结果为 $1.1/(-0.9) \times 1\text{KB} \times (1 - (1/100000)^{0.9}) \approx -1.22\text{KB}$，此负值表明公式在 $\alpha<2$ 时发散，需改用积分形式 $\int_{s_{min}}^{s_{max}} s \cdot f_S(s) ds$ 直接计算，结果为 $\frac{s_{max}^{2-\alpha} - s_{min}^{2-\alpha}}{2-\alpha} \cdot (\alpha-1) s_{min}^{\alpha-1}$。

## Corrected Claim

Pareto分布截断均值 $E[S]_{trunc}$ 的精确计算公式为 $E[S]_{trunc} = \frac{\alpha-1}{\alpha-2} s_{min} (1 - (s_{min}/s_{max})^{2-\alpha})$，当 $\alpha=1.1, s_{min}=1\text{KB}, s_{max}=100\text{MB}$ 时，计算结果为 $1.1/(-0.9) \times 1\text{KB} \times (1 - (1/100000)^{0.9}) \approx -1.22\text{KB}$，此负值表明公式在 $\alpha<2$ 时发散，需改用积分形式 $\int_{s_{min}}^{s_{max}} s \cdot f_S(s) ds$ 直接计算，结果为 $\frac{s_{max}^{2-\alpha} - s_{min}^{2-\alpha}}{2-\alpha} \cdot (\alpha-1) s_{min}^{\alpha-1}$。
