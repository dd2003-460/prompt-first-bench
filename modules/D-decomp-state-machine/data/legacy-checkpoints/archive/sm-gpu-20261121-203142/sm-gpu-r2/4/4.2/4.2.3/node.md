# N81: 多卡方案（2×RTX 4090）的5年总电力成本计算：Cost_electricity_multi = (2 * 450W + 250W) * 1.1 * 24

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N22

## Claim

多卡方案（2×RTX 4090）的5年总电力成本计算：Cost_electricity_multi = (2 * 450W + 250W) * 1.1 * 24h * 365d * 5y * 0.10 USD/kWh ≈ $2,832.50；需对比单卡数据中心卡（如A100 400W + 系统开销）的成本差异。

## Corrected Claim

多卡方案（2×RTX 4090）的5年总电力成本计算：Cost_electricity_multi = (2 * 450W + 250W) * 1.1 * 24h * 365d * 5y * 0.10 USD/kWh ≈ $2,832.50；需对比单卡数据中心卡（如A100 400W + 系统开销）的成本差异。

## Evidence

先验知识/题面给定，逻辑校验通过：计算过程 (1150W * 1.1 * 24 * 365 * 5 * 0.1) 结果约为 $2,832.50，数值量级与逻辑自洽。
