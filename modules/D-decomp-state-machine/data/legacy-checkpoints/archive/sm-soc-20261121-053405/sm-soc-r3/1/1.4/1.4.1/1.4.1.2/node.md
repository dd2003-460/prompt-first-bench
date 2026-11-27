# N102: 基准流量参数 λ_base 的量化：定义为平台在无任何溢价加成（P_ask = μ_p）时的平均每小时咨询到达率，通常需基于历史日志回归估计，初始假设值可设为 

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N30

## Claim

基准流量参数 λ_base 的量化：定义为平台在无任何溢价加成（P_ask = μ_p）时的平均每小时咨询到达率，通常需基于历史日志回归估计，初始假设值可设为 0.05/h（对应日均约1.2次咨询/件）。

## Corrected Claim

基准流量参数 λ_base 的量化：定义为平台在无任何溢价加成（P_ask = μ_p）时的平均每小时咨询到达率，通常需基于历史日志回归估计，初始假设值可设为 0.05/h（对应日均约1.2次咨询/件）。

## Evidence

先验知识/题面给定，逻辑校验通过：0.05/h * 24h = 1.2次/日，数值换算准确，定义符合排队论/流量建模常规假设。

## Search Query

baseline inquiry rate per hour second-hand marketplace
