# N364: 市场流动性 L 的量化定义与基准值。L 定义为日均成交量与挂牌库存量的比值（L = Daily_Transactions / Active_Listings）。

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N110

## Claim

市场流动性 L 的量化定义与基准值。L 定义为日均成交量与挂牌库存量的比值（L = Daily_Transactions / Active_Listings）。在主流二手平台，L 通常介于 0.05-0.2 之间。若 L=0.1 且 ΔP_band=0.2，则 σ²_crit = 0.1 * 0.04 / (1 - 0.3) ≈ 0.0057，对应 σ_crit ≈ 0.075。

## Corrected Claim

市场流动性 L 的量化定义与基准值。L 定义为日均成交量与挂牌库存量的比值（L = Daily_Transactions / Active_Listings）。在主流二手平台，L 通常介于 0.05-0.2 之间。若 L=0.1 且 ΔP_band=0.2，则 σ²_crit = 0.1 * 0.04 / (1 - 0.3) ≈ 0.0057，对应 σ_crit ≈ 0.075。

## Evidence

先验知识/题面给定，逻辑校验通过：公式推导 σ²_crit = 0.1 * 0.04 / 0.7 ≈ 0.00571，开方后 σ_crit ≈ 0.0755，数值量级与逻辑自洽。
