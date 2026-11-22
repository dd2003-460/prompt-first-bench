# N86: 基于 Clayton Copula 参数 θ = 2.03（由 ρ=-0.3 映射得出），联合分布下对象大小与热度的条件期望 E[S|P] 需通过数值积分计算，

- **status**: degraded
- **level**: L3
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: (root)

## Claim

基于 Clayton Copula 参数 θ = 2.03（由 ρ=-0.3 映射得出），联合分布下对象大小与热度的条件期望 E[S|P] 需通过数值积分计算，解析近似为 E[S|P] ≈ E[S] * (1 + ρ * (P/E[P] - 1) * κ)，其中 κ 为分布形状修正因子，用于量化负相关对缓存空间利用的具体影响。

## Corrected Claim

基于 Clayton Copula 参数 θ = 2.03（由 ρ=-0.3 映射得出），联合分布下对象大小与热度的条件期望 E[S|P] 需通过数值积分计算，解析近似为 E[S|P] ≈ E[S] * (1 + ρ * (P/E[P] - 1) * κ)，其中 κ 为分布形状修正因子，用于量化负相关对缓存空间利用的具体影响。

## Evidence

检索失败: no sources from any channel (all 5 failed)
