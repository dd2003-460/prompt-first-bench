# N276: 2x RTX 4090 方案的 5 年 OpEx 修正值：OpEx_5yr_corrected = 5 * (2 * P_avg_fp8 * 8760 * $0

- **status**: degraded
- **level**: L4
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N99, N100, N101

## Claim

2x RTX 4090 方案的 5 年 OpEx 修正值：OpEx_5yr_corrected = 5 * (2 * P_avg_fp8 * 8760 * $0.15)，其中 P_avg_fp8 为 FP8 推理平均功耗，需从 N134 获取实测数据（预计 350-400W），替代 N99 中使用的 450W TDP 上限，以反映真实能耗成本。

## Corrected Claim

2x RTX 4090 方案的 5 年 OpEx 修正值计算公式为：OpEx_5yr_corrected = 5 * (2 * P_avg_fp8 * 8760 * $0.15)。其中 P_avg_fp8 为 FP8 推理平均功耗，需依据实测数据（参考范围约 350-400W）替代 TDP 上限以反映真实能耗成本。

## Evidence

[质询]该陈述包含具体的硬件功耗预期值（350-400W）和电价参数（$0.15），属于经验事实。虽然逻辑公式自洽，但缺乏外部来源直接支持具体的功耗实测数据或电价标准，且‘预计’一词表明这是基于假设的估算而非已验证事实。 | 经验事实，逻辑自洽但缺来源支持（检索无可用来源，无法验证具体功耗数值和电价参数的准确性）

## Search Query

RTX 4090 average power consumption FP8 inference 27B model watts
