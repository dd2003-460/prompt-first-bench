# N544: RTX 4090 在 CUDA 12.4+ 环境下，使用 llama.cpp 进行 Qwen3-27B INT4 推理时，软件栈损耗系数约为 85-90%，实际

- **status**: degraded
- **level**: L5
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 1
- **parent_ids**: N169

## Claim

RTX 4090 在 CUDA 12.4+ 环境下，使用 llama.cpp 进行 Qwen3-27B INT4 推理时，软件栈损耗系数约为 85-90%，实际吞吐约为 63.4 * 0.85 ≈ 53.9 tokens/s 至 67.1 * 0.90 ≈ 60.4 tokens/s。

## Corrected Claim

RTX 4090 在 CUDA 12.4+ 环境下，使用 llama.cpp 进行 Qwen3-27B INT4 推理时，实际吞吐受软件栈效率影响，具体数值需依据实测基准确定，通常显著低于理论峰值。

## Evidence

[质询]软件栈损耗系数（85-90%）及具体吞吐数值（53.9-60.4 tokens/s）属于高度依赖具体硬件配置、驱动版本、llama.cpp 编译参数及量化实现细节的经验性数据，无法从第一性原理推导，且缺乏通用基准测试支持该特定区间。 | 经验事实，逻辑自洽但缺来源支持
