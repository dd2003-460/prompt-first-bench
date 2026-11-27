# N178: RTX 5090 在 W4 精度下运行 Qwen3-27B 的预填充阶段 (32K 上下文) 计算瓶颈耗时理论值需基于其 Blackwell 架构的 TFLOP

- **status**: degraded
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N47

## Claim

RTX 5090 在 W4 精度下运行 Qwen3-27B 的预填充阶段 (32K 上下文) 计算瓶颈耗时理论值需基于其 Blackwell 架构的 TFLOPS 计算，假设其 FP16 TFLOPS 为 RTX 4090 的 1.5 倍 (123.9 TFLOPS)，考虑 50% MFU 后耗时为 28.6 秒 (1.77 TFLOPs / 61.95 TFLOPS)，具体需核验实际算力参数。

## Corrected Claim

RTX 5090 在 W4 精度下运行 Qwen3-27B 的预填充阶段 (32K 上下文) 计算瓶颈耗时理论值需基于其 Blackwell 架构的实际 TFLOPS 计算，具体数值需依据官方发布的硬件规格及实测 MFU 进行核验。

## Evidence

[质询]RTX 5090 的 FP16 算力参数（123.9 TFLOPS）及由此推导的耗时（28.6秒）属于具体硬件规格与性能指标，无法仅凭逻辑推导得出，且缺乏外部来源直接支持该特定数值假设。 | 经验事实，逻辑自洽但缺来源支持

## Search Query

RTX 5090 FP16 TFLOPS Qwen3-27B 32K prefill time
