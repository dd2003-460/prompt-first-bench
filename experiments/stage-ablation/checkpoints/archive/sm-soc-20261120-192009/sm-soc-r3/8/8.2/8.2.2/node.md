# N323: 异常值剔除规则：基于同类商品过去 7 天成交价的 IQR 方法，剔除 Price < P25 - 1.5*IQR 或 Price > P75 + 1.5*IQR

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N110

## Claim

异常值剔除规则：基于同类商品过去 7 天成交价的 IQR 方法，剔除 Price < P25 - 1.5*IQR 或 Price > P75 + 1.5*IQR 的交易记录；若剔除后样本量 N_clean < N_sample * 0.7，则标记该组数据为 [低置信] 并扩大时间窗口至 14 天。

## Corrected Claim

异常值剔除规则：基于同类商品过去 7 天成交价的 IQR 方法，剔除 Price < P25 - 1.5*IQR 或 Price > P75 + 1.5*IQR 的交易记录；若剔除后样本量 N_clean < N_sample * 0.7，则标记该组数据为 [低置信] 并扩大时间窗口至 14 天。

## Evidence

先验知识/题面给定，逻辑校验通过
