# N24: Pareto(α=1.1) 分布下，前 k 个最小对象的总大小占总体大小的比例公式为 (1 - (k/N)^{α-1}) / (α-1) 的变体，具体为 Siz

- **status**: degraded
- **level**: L2
- **source**: search
- **edge_type**: quotient
- **rework_count**: 1
- **parent_ids**: (root)

## Claim

Pareto(α=1.1) 分布下，前 k 个最小对象的总大小占总体大小的比例公式为 (1 - (k/N)^{α-1}) / (α-1) 的变体，具体为 Size_Fraction(k) = 1 - (k/N)^{α-1} (当 α>1 且考虑累积质量时，需修正为积分形式：∫_{s_min}^{s_k} x^{-α} dx / ∫_{s_min}^{∞} x^{-α} dx = 1 - (s_min/s_k)^{α-1})，由于 ρ=-0.3，缓存优先容纳的小对象在字节命中率计算中权重需按此比例调整。

## Corrected Claim

Pareto(α=1.1) 分布下，前 k 个最小对象的总大小占总体大小的比例公式为 (1 - (k/N)^{α-1}) / (α-1) 的变体，具体为 Size_Fraction(k) = 1 - (k/N)^{α-1} (当 α>1 且考虑累积质量时，需修正为积分形式：∫_{s_min}^{s_k} x^{-α} dx / ∫_{s_min}^{∞} x^{-α} dx = 1 - (s_min/s_k)^{α-1})，由于 ρ=-0.3，缓存优先容纳的小对象在字节命中率计算中权重需按此比例调整。

## Evidence

检索失败: no sources from any channel (all 5 failed)
