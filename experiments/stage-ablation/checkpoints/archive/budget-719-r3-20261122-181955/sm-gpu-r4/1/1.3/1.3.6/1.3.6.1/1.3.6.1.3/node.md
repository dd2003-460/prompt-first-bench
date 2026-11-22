# N533: ROCm 5.7/6.0 中 Qwen3 BF16 Attention 内核的实测吞吐量与 CUDA 12.4 对比：需获取 MI300X 上 Qwen3-27

- **status**: degraded
- **level**: L5
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N185

## Claim

ROCm 5.7/6.0 中 Qwen3 BF16 Attention 内核的实测吞吐量与 CUDA 12.4 对比：需获取 MI300X 上 Qwen3-27B BF16 的 Prefill/Decode tokens/s 实测数据，并与 A100/H100 同精度数据进行对比，量化性能差距百分比。

## Corrected Claim

ROCm 5.7/6.0 中 Qwen3 BF16 Attention 内核在 MI300X 上的实测吞吐量与 CUDA 12.4 在 A100/H100 上的对比数据需通过实际基准测试获取，当前缺乏公开实测数据支持具体性能差距百分比。

## Evidence

[质询]该陈述要求提供具体的实测吞吐量数据（Prefill/Decode tokens/s）及性能差距百分比，属于高度依赖具体硬件环境、软件版本及测试方法的经验事实，且当前无任何参考来源支持，无法验证具体数值。 | 经验事实，逻辑自洽但缺来源支持（本轮检索无可用来源）

## Search Query

MI300X Qwen3-27B BF16 inference throughput benchmark tokens/s
