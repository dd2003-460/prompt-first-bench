# N534: MI300X 上 GPTQ INT4 量化 Qwen3-27B 的实测 Decode 吞吐量：需获取具体数值（tokens/s），并与 CUDA 平台（如 A1

- **status**: degraded
- **level**: L5
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N186

## Claim

MI300X 上 GPTQ INT4 量化 Qwen3-27B 的实测 Decode 吞吐量：需获取具体数值（tokens/s），并与 CUDA 平台（如 A100/H100）上同等 GPTQ INT4 方案的吞吐量进行对比，计算性能损失百分比。

## Corrected Claim

MI300X 上 GPTQ INT4 量化 Qwen3-27B 的 Decode 吞吐量需通过实际基准测试获取，并与 CUDA 平台（如 A100/H100）同等方案对比以评估性能差异；目前缺乏公开统一的实测数值，无法直接给出具体 tokens/s 及性能损失百分比。

## Evidence

[质询]该陈述要求提供具体的实测吞吐量数值（tokens/s）及性能损失百分比，属于具体的经验性能数据。由于缺乏实测基准测试数据，无法确定具体数值，且不同硬件配置、软件栈版本及并发设置会导致结果差异巨大，直接断言具体数值缺乏依据。 | 经验事实，逻辑自洽但缺来源支持（检索无可用来源，且具体性能数值无法从第一性原理推导）。

## Search Query

MI300X GPTQ INT4 Qwen3-27B decode throughput benchmark
