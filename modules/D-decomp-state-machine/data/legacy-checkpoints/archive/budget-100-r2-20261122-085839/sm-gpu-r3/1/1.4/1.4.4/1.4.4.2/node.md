# N153: RTX 3090 不支持 FP8 Tensor Core，仅支持 INT8/INT4 Tensor Core，因此无法利用 FP8 KV Cache 的硬件加速

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N43

## Claim

RTX 3090 不支持 FP8 Tensor Core，仅支持 INT8/INT4 Tensor Core，因此无法利用 FP8 KV Cache 的硬件加速，只能使用 INT8 KV (无硬件加速优势) 或 BF16 KV，导致其在 KV Cache 量化方案上性能低于 RTX 4090。

## Corrected Claim

RTX 3090 不支持 FP8 Tensor Core，仅支持 INT8/INT4 Tensor Core，因此无法利用 FP8 KV Cache 的硬件加速，只能使用 INT8 KV (无硬件加速优势) 或 BF16 KV，导致其在 KV Cache 量化方案上性能低于 RTX 4090。

## Evidence

先验知识/题面给定，逻辑校验通过：RTX 3090 (Ampere架构) 确实不支持FP8 Tensor Core，仅支持INT8/INT4，而RTX 4090 (Ada Lovelace架构) 支持FP8，因此3090在FP8 KV Cache加速上确实落后。
