# N75: 负相关修正因子 K(ρ) 的精确计算：K(ρ) = E[S|H∈Top-k] / E[S|H∈Random]。对于 ρ=-0.3，K(ρ) < 1，具体值取决于

- **status**: degraded
- **level**: L3
- **source**: search
- **edge_type**: quotient
- **rework_count**: 1
- **parent_ids**: N27

## Claim

负相关修正因子 K(ρ) 的精确计算：K(ρ) = E[S|H∈Top-k] / E[S|H∈Random]。对于 ρ=-0.3，K(ρ) < 1，具体值取决于 k_eff/N 的比例。若 k_eff/N = 0.1，K(ρ) ≈ 0.85；若 k_eff/N = 0.5，K(ρ) ≈ 0.92。此因子直接乘在独立假设的命中率上，得到 H_byte_corr = H_byte_indep * K(ρ)。

## Corrected Claim

负相关修正因子 K(ρ) 定义为条件期望之比 K(ρ) = E[S|H∈Top-k] / E[S|H∈Random]。对于 ρ=-0.3，K(ρ) < 1，其具体数值取决于 k_eff/N 的比例及底层分布假设。此因子直接乘在独立假设的命中率上，得到 H_byte_corr = H_byte_indep * K(ρ)。

## Evidence

[质询]该陈述给出了具体的数值近似（如 k_eff/N=0.1 时 K≈0.85），这属于经验事实或特定分布假设下的计算结果，无法仅从第一性原理（如仅知道 ρ=-0.3）严格推出，且缺乏来源支持其具体数值的准确性。 | 经验事实，逻辑自洽但缺来源支持

## Search Query

size popularity correlation cache hit rate reduction factor quantification
