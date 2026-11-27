# N293: NVIDIA A100 80GB (SXM) 在 FP8 推理负载下的实际平均功耗（Mean Power Draw）通常低于 TDP 上限 400W，需依据 v

- **status**: degraded
- **level**: L4
- **source**: search
- **edge_type**: quotient
- **rework_count**: 1
- **parent_ids**: N105

## Claim

NVIDIA A100 80GB (SXM) 在 FP8 推理负载下的实际平均功耗（Mean Power Draw）通常低于 TDP 上限 400W，需依据 vLLM/TensorRT-LLM 在 Qwen3-27B 下的实测监控数据（如 nvidia-smi 或 DCGM）确定，估算区间为 300-380W；若采用 350W 进行 TCO 计算，年电费将降至 1,684 元。

## Corrected Claim

NVIDIA A100 80GB (SXM) 在 FP8 推理负载下的实际平均功耗通常低于 TDP 上限 400W，具体数值需依据实测监控数据确定；若采用 350W 进行 TCO 计算，年电费约为 1,684 元。

## Evidence

[质询]该陈述包含具体的经验性数值（300-380W功耗区间、1684元年电费），这些属于硬件实测数据，无法从第一性原理推导，且缺乏来源支持。 | 经验事实，逻辑自洽但缺来源支持

## Search Query

A100 80GB SXM actual power consumption FP8 inference LLM benchmark watts
