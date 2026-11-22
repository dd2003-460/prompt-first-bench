# N318: 2×RTX 4090 (FP8) 在 Batch Size=1, 32K输入/1K输出下的实测吞吐量上限：在最优框架配置（如SGLang + FlashAtte

- **status**: degraded
- **level**: L4
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N88

## Claim

2×RTX 4090 (FP8) 在 Batch Size=1, 32K输入/1K输出下的实测吞吐量上限：在最优框架配置（如SGLang + FlashAttention-2 + FP8 KV Cache）下，Qwen3-27B在双卡RTX 4090上的实测吞吐量上限约为 15-25 tokens/s [search: 需检索最新优化结果]，接近父节点预估的上限，但需依赖特定的内存优化和通信重叠技术。

## Corrected Claim

2×RTX 4090 (FP8) 在 Batch Size=1, 32K输入/1K输出下，Qwen3-27B的实测吞吐量受内存带宽和计算效率限制，具体数值需依赖特定框架（如SGLang）及优化技术（FlashAttention-2, FP8 KV Cache）的实测数据，预估范围约为 15-25 tokens/s，但需以实际基准测试为准。

## Evidence

[质询]该数值属于特定硬件配置下的经验性能指标，缺乏公开权威基准测试的直接支持，且不同框架/驱动版本下波动较大，存在将理论峰值或特定优化场景误标为通用上限的风险。 | 经验事实，逻辑自洽但缺来源支持（检索无可用来源，无法验证具体数值区间）

## Search Query

SGLang RTX 4090 Qwen3-27B FP8 32k context throughput optimization
