# N229: 最小可检测效应 E 的绝对值计算：E = 0.05 * μ_revenue，其中 μ_revenue 为卖家平均月收入，若 μ_revenue = 1000 元

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N82

## Claim

最小可检测效应 E 的绝对值计算：E = 0.05 * μ_revenue，其中 μ_revenue 为卖家平均月收入，若 μ_revenue = 1000 元，则 E = 50 元；该效应量需与统计功效 Power=0.8 联合确定 n_min，而非独立设定。

## Corrected Claim

最小可检测效应 E 的绝对值计算：E = 0.05 * μ_revenue，其中 μ_revenue 为卖家平均月收入，若 μ_revenue = 1000 元，则 E = 50 元；该效应量需与统计功效 Power=0.8 联合确定 n_min，而非独立设定。

## Evidence

先验知识/题面给定，逻辑校验通过：效应量定义为均值的一定比例（5%）符合常规统计功效分析设定，数值计算（1000*0.05=50）正确，且效应量与功效联合确定样本量是标准统计流程。

## Search Query

minimum detectable effect calculation A/B test revenue metric
