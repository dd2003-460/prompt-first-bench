# N402: NVIDIA L40S 在运行 27B 参数模型进行 Batch Size=1 自回归解码时的稳态平均功耗 (P_avg_decode) 实测值，预期在 180

- **status**: degraded
- **level**: L4
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N129

## Claim

NVIDIA L40S 在运行 27B 参数模型进行 Batch Size=1 自回归解码时的稳态平均功耗 (P_avg_decode) 实测值，预期在 180W-240W 区间，需引用具体硬件功耗监测日志或第三方评测。

## Corrected Claim

NVIDIA L40S 在运行 27B 参数模型进行 Batch Size=1 自回归解码时的稳态平均功耗 (P_avg_decode) 预期在 180W-240W 区间（待验证）。

## Evidence

[质询]该陈述包含具体的经验性数值区间（180W-240W），属于硬件功耗实测数据，无法从第一性原理推导，且缺乏来源支持。 | 经验事实，逻辑自洽但缺来源支持

## Search Query

NVIDIA L40S average power consumption LLM inference 27B batch size 1 decode
