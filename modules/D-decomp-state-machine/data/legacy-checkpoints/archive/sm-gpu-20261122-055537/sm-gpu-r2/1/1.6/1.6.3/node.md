# N55: KV Cache 量化选项对显存的影响：若使用 FP8 或 INT8 存储 KV Cache（如 vLLM 的 paged attention 支持），显存占用

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N12

## Claim

KV Cache 量化选项对显存的影响：若使用 FP8 或 INT8 存储 KV Cache（如 vLLM 的 paged attention 支持），显存占用减半，即 BF16 的 7.25 GB 降至 ~3.6 GB (FP8) 或 ~3.6 GB (INT8)，这显著改变 24GB 显卡的可行性边界

## Corrected Claim

KV Cache 量化选项对显存的影响：若使用 FP8 或 INT8 存储 KV Cache（如 vLLM 的 paged attention 支持），显存占用减半，即 BF16 的 7.25 GB 降至 ~3.6 GB (FP8) 或 ~3.6 GB (INT8)，这显著改变 24GB 显卡的可行性边界

## Evidence

先验知识/题面给定，逻辑校验通过：FP8/INT8 为 8-bit 格式，BF16 为 16-bit 格式，数据量减半符合数学逻辑（7.25GB / 2 ≈ 3.625GB），且 vLLM 确实支持 KV Cache 量化以节省显存。

## Search Query

vLLM KV cache quantization FP8 INT8 memory savings 32k context
