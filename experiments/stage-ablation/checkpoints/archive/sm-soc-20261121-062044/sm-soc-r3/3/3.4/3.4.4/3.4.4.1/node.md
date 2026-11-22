# N186: NPV 时间步长 t 的确定：t 为月度，需设定预测 horizon T_max = 36 个月 (3 年)，因为二手平台卖家生命周期通常 < 3 年；若 T_

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N68

## Claim

NPV 时间步长 t 的确定：t 为月度，需设定预测 horizon T_max = 36 个月 (3 年)，因为二手平台卖家生命周期通常 < 3 年；若 T_max < 12 个月，则忽略长期留存效应；若 T_max > 36 个月，则远期折现因子 (1+r)^t 过小，噪声主导，需截断。

## Corrected Claim

NPV 时间步长 t 的确定：t 为月度，需设定预测 horizon T_max = 36 个月 (3 年)，因为二手平台卖家生命周期通常 < 3 年；若 T_max < 12 个月，则忽略长期留存效应；若 T_max > 36 个月，则远期折现因子 (1+r)^t 过小，噪声主导，需截断。

## Evidence

先验知识/题面给定，逻辑校验通过：36个月作为二手平台卖家生命周期上限符合商业直觉，且关于折现因子噪声主导的截断逻辑在金融建模中自洽。
