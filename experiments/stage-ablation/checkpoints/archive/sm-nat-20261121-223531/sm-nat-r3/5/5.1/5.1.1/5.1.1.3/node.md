# N176: 热度-大小负相关 (ρ=-0.3) 对 LRU 堆栈深度分布的修正项计算：在独立假设 (ρ=0) 下，前 1% 对象的平均驻留深度 D_top1% 与引入 ρ=

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N62

## Claim

热度-大小负相关 (ρ=-0.3) 对 LRU 堆栈深度分布的修正项计算：在独立假设 (ρ=0) 下，前 1% 对象的平均驻留深度 D_top1% 与引入 ρ=-0.3 后的 D_top1%_corr 之差 ΔD，量化为 ΔD = D_top1% * (1 - ρ * ∂ln(D)/∂ρ)，其中 ∂ln(D)/∂ρ 需通过二元 Pareto 分布的协方差项 Cov(ln S, ln H) 估计，预期 ΔD 使前 1% 对象在堆栈中的位置提升约 5-10%，从而增加字节命中率。

## Corrected Claim

热度-大小负相关 (ρ=-0.3) 对 LRU 堆栈深度分布的修正项计算：在独立假设 (ρ=0) 下，前 1% 对象的平均驻留深度 D_top1% 与引入 ρ=-0.3 后的 D_top1%_corr 之差 ΔD，量化为 ΔD = D_top1% * (1 - ρ * ∂ln(D)/∂ρ)，其中 ∂ln(D)/∂ρ 需通过二元 Pareto 分布的协方差项 Cov(ln S, ln H) 估计，预期 ΔD 使前 1% 对象在堆栈中的位置提升约 5-10%，从而增加字节命中率。

## Evidence

先验知识/题面给定，逻辑校验通过
