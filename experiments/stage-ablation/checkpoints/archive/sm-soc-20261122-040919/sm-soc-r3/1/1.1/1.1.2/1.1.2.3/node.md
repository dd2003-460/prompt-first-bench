# N132: 信息缺失方差 σ²_info 的量化：σ²_info = σ²_market / n_samples，其中 σ²_market 为同类商品成交价的总体方差，n_

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N32

## Claim

信息缺失方差 σ²_info 的量化：σ²_info = σ²_market / n_samples，其中 σ²_market 为同类商品成交价的总体方差，n_samples 为卖家可获取的近期成交数据样本量。

## Corrected Claim

信息缺失方差 σ²_info 的量化：σ²_info = σ²_market / n_samples，其中 σ²_market 为同类商品成交价的总体方差，n_samples 为卖家可获取的近期成交数据样本量。

## Evidence

先验知识/题面给定，逻辑校验通过：该公式符合统计学中样本均值方差（Var(X̄) = σ²/n）的基本定义，量纲与逻辑自洽。

## Search Query

estimation error variance formula sample size market price variance
