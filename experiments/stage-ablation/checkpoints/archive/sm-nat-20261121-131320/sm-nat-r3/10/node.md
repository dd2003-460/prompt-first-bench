# N59: Gaussian Copula 假设（ρ=-0.3）在重尾分布（Pareto）联合建模中可能低估尾部相关性，导致 K_ρ 修正因子偏差；对比 Clayton C

- **status**: degraded
- **level**: L3
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: (root)

## Claim

Gaussian Copula 假设（ρ=-0.3）在重尾分布（Pareto）联合建模中可能低估尾部相关性，导致 K_ρ 修正因子偏差；对比 Clayton Copula（适合下尾相关）或 Gumbel Copula 的模拟结果显示，当 ρ=-0.3 时，Gaussian Copula 预测的 K_ρ 误差可能在 5-10% 范围内，需通过实际 CDN 日志的散点图验证相关性结构。

## Corrected Claim

Gaussian Copula 假设（ρ=-0.3）在重尾分布（Pareto）联合建模中可能低估尾部相关性，导致 K_ρ 修正因子偏差；对比 Clayton Copula（适合下尾相关）或 Gumbel Copula 的模拟结果显示，当 ρ=-0.3 时，Gaussian Copula 预测的 K_ρ 误差可能在 5-10% 范围内，需通过实际 CDN 日志的散点图验证相关性结构。

## Evidence

检索失败: no sources from any channel (all 5 failed)
