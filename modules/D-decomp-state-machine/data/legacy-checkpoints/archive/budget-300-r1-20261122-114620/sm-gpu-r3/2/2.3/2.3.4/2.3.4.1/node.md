# N213: Apple M2 Ultra (192GB) 运行 Qwen3-27B FP8 时，理论峰值吞吐 29.6 t/s (800GB/s / 27GB)，但实际受限

- **status**: degraded
- **level**: L4
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N65

## Claim

Apple M2 Ultra (192GB) 运行 Qwen3-27B FP8 时，理论峰值吞吐 29.6 t/s (800GB/s / 27GB)，但实际受限于 CPU-GPU 统一内存控制器调度，实测吞吐通常降至理论值的 60-70%，即 17.8-20.7 t/s，此数值需通过 llama.cpp 或 MLX 框架在 Mac Studio M2 Ultra 上实测核验。

## Corrected Claim

Apple M2 Ultra (192GB) 运行 Qwen3-27B FP8 时，理论峰值吞吐约为 29.6 t/s (800GB/s / 27GB)。实际吞吐受内存控制器调度等因素限制，通常低于理论值，具体数值需通过 llama.cpp 或 MLX 框架在 Mac Studio M2 Ultra 上实测核验。

## Evidence

[质询]该陈述包含具体的经验性性能数据（60-70%的效率损耗比例及对应的17.8-20.7 t/s实测值），属于特定硬件与软件栈组合下的经验事实，无法从第一性原理严格推导，且缺乏来源支持。 | 经验事实，逻辑自洽但缺来源支持（检索无可用来源）

## Search Query

Apple M2 Ultra Qwen3 27B inference throughput tokens per second benchmark
