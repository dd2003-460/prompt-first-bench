# N64: 统计显著性检验的具体执行方案：对 $\eta$ 进行 Bootstrap 重抽样（n=10000次），计算其95%置信区间。若置信区间不包含0且下限 $\eta

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N24

## Claim

统计显著性检验的具体执行方案：对 $\eta$ 进行 Bootstrap 重抽样（n=10000次），计算其95%置信区间。若置信区间不包含0且下限 $\eta_{lower} > 0$，则判定为‘统计显著为正’；同时需计算 $\eta$ 在不同时间窗口（周/月）的变异系数 $CV(\eta) < 0.2$ 以验证‘稳定性’。

## Corrected Claim

统计显著性检验的具体执行方案：对 $\eta$ 进行 Bootstrap 重抽样（n=10000次），计算其95%置信区间。若置信区间不包含0且下限 $\eta_{lower} > 0$，则判定为‘统计显著为正’；同时需计算 $\eta$ 在不同时间窗口（周/月）的变异系数 $CV(\eta) < 0.2$ 以验证‘稳定性’。

## Evidence

先验知识/题面给定，逻辑校验通过
