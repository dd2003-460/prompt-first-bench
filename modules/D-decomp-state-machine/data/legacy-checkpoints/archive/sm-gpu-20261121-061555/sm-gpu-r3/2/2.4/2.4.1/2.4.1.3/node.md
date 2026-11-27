# N198: Qwen3-27B 在 BF16 精度下的运行时开销（Overhead）显存占用：包括 CUDA 上下文、算子中间缓冲、Fragmentation 等，通常估算

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N65

## Claim

Qwen3-27B 在 BF16 精度下的运行时开销（Overhead）显存占用：包括 CUDA 上下文、算子中间缓冲、Fragmentation 等，通常估算为权重显存的 5-10% 或固定 2-4 GB。取保守值 3.5 GB 作为基准。

## Corrected Claim

Qwen3-27B 在 BF16 精度下的运行时开销（Overhead）显存占用：包括 CUDA 上下文、算子中间缓冲、Fragmentation 等，通常估算为权重显存的 5-10% 或固定 2-4 GB。取保守值 3.5 GB 作为基准。

## Evidence

先验知识/题面给定，逻辑校验通过
