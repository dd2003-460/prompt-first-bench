# N401: NVIDIA A100 80GB (SXM/PCIe) 在运行 27B 参数模型进行 Batch Size=1 自回归解码时的稳态平均功耗 (P_avg_dec

- **status**: degraded
- **level**: L4
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N129

## Claim

NVIDIA A100 80GB (SXM/PCIe) 在运行 27B 参数模型进行 Batch Size=1 自回归解码时的稳态平均功耗 (P_avg_decode) 实测值，预期在 250W-320W 区间，需引用 MLPerf 或特定框架 (vLLM/TensorRT) 的能效基准测试数据。

## Corrected Claim

NVIDIA A100 80GB 在运行 27B 参数模型进行 Batch Size=1 自回归解码时的稳态平均功耗通常在 250W-320W 区间，具体数值需参考 MLPerf 或 vLLM/TensorRT 等框架的能效基准测试数据。

## Evidence

[质询]该陈述包含具体的经验性数值区间（250W-320W）和特定测试条件（Batch Size=1, 27B模型），属于硬件功耗的经验事实，无法从第一性原理严格推导，且缺乏来源支持。 | 经验事实，逻辑自洽但缺来源支持（检索无可用来源）

## Search Query

NVIDIA A100 80GB average power consumption LLM inference 27B batch size 1 decode
