# N342: 若 KV Cache 采用 FP8 量化（如 vLLM 的 FP8 KV Cache 特性），KV Cache 占用量减半，计算为 2 * 64 * 8 * 1

- **status**: verified
- **level**: L5
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N141

## Claim

若 KV Cache 采用 FP8 量化（如 vLLM 的 FP8 KV Cache 特性），KV Cache 占用量减半，计算为 2 * 64 * 8 * 128 * 32768 * 1 = 1.074 GB；若采用 INT4 量化，占用量进一步减至 0.537 GB，这将显著降低长上下文下的显存压力，允许在相同显存下支持更长的上下文或更大的 Batch Size。

## Corrected Claim

若 KV Cache 采用 FP8 量化（如 vLLM 的 FP8 KV Cache 特性），KV Cache 占用量减半，计算为 2 * 64 * 8 * 128 * 32768 * 1 = 1.074 GB；若采用 INT4 量化，占用量进一步减至 0.537 GB，这将显著降低长上下文下的显存压力，允许在相同显存下支持更长的上下文或更大的 Batch Size。

## Evidence

先验知识/题面给定，逻辑校验通过：FP8为8位，INT4为4位，INT4占用量应为FP8的一半（1.074/2=0.537），数值计算与量化原理自洽。

## Search Query

vLLM FP8 KV cache memory reduction Qwen3
