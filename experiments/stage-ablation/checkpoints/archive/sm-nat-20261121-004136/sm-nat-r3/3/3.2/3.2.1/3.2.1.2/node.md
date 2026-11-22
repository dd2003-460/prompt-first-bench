# N119: 负相关工作点（ρ=-0.3）下的 LFU 增益 Δ_H_ρ=-0.3 的修正值：由于热门对象较小，LRU 在 ρ=-0.3 下的命中率 H_LRU_ρ=-0.3

- **status**: degraded
- **level**: L4
- **source**: search
- **edge_type**: quotient
- **rework_count**: 1
- **parent_ids**: N46

## Claim

负相关工作点（ρ=-0.3）下的 LFU 增益 Δ_H_ρ=-0.3 的修正值：由于热门对象较小，LRU 在 ρ=-0.3 下的命中率 H_LRU_ρ=-0.3 高于 H_LRU_ρ=0（因小对象占据空间少，驱逐少），导致 LFU 的相对增益空间被压缩。量化修正：Δ_H_ρ=-0.3 ≈ Δ_H_ρ=0 * (1 - |ρ| * (σ_size/σ_rank) * Sensitivity_Factor)，其中 Sensitivity_Factor 需通过 Copula 模型模拟确定，估算值约为 0.8-0.9，故 Δ_H_ρ=-0.3 ≈ 0.0013-0.0015。

## Corrected Claim

在负相关工作点（ρ=-0.3）下，由于热门对象较小，LRU 命中率高于 ρ=0 时的情况，导致 LFU 的相对增益空间被压缩。理论上，Δ_H_ρ=-0.3 应小于 Δ_H_ρ=0，具体修正系数需通过 Copula 模型模拟确定，估算值约为 0.0013-0.0015（待实证验证）。

## Evidence

[质询]该陈述包含具体的经验性数值（Sensitivity_Factor 0.8-0.9 及最终增益 0.0013-0.0015），这些参数无法从第一性原理或数学公理严格推导，属于依赖特定负载分布和系统配置的实证数据，且缺乏来源支持。 | 经验事实，逻辑自洽但缺来源支持（检索无可用来源，且具体数值无法从第一性原理推出）

## Search Query

impact of size-popularity correlation on LFU vs LRU cache hit rate simulation
