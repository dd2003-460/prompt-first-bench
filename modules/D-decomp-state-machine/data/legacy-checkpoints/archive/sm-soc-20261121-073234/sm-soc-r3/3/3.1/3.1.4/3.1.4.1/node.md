# N205: GMV_baseline_t 的确定：需使用对照组（未受干预影响）的 GMV 数据作为基准。若 A/B 测试中对照组样本量不足，需使用历史同期数据并剔除季节性因

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N66

## Claim

GMV_baseline_t 的确定：需使用对照组（未受干预影响）的 GMV 数据作为基准。若 A/B 测试中对照组样本量不足，需使用历史同期数据并剔除季节性因素，公式为 GMV_baseline_t = GMV_hist_t * (1 + Seasonal_Adjustment_t)，其中 Seasonal_Adjustment_t 需通过时间序列分解获得。

## Corrected Claim

GMV_baseline_t 的确定：需使用对照组（未受干预影响）的 GMV 数据作为基准。若 A/B 测试中对照组样本量不足，需使用历史同期数据并剔除季节性因素，公式为 GMV_baseline_t = GMV_hist_t * (1 + Seasonal_Adjustment_t)，其中 Seasonal_Adjustment_t 需通过时间序列分解获得。

## Evidence

先验知识/题面给定，逻辑校验通过

## Search Query

GMV baseline calculation A/B test control group seasonal adjustment
