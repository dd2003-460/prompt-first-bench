# N65: NVIDIA RTX 4090D 在 FP8 精度下运行 Qwen3-27B 时的显存占用约为 27GB (权重) + KV Cache，若 KV Cache 

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N8

## Claim

NVIDIA RTX 4090D 在 FP8 精度下运行 Qwen3-27B 时的显存占用约为 27GB (权重) + KV Cache，若 KV Cache 为 FP8 且 32K 上下文，总占用约为 40.8GB，超出 24GB 显存，必须使用 Offloading 或更激进的量化

## Corrected Claim

NVIDIA RTX 4090D 在 FP8 精度下运行 Qwen3-27B 时的显存占用约为 27GB (权重) + KV Cache，若 KV Cache 为 FP8 且 32K 上下文，总占用约为 40.8GB，超出 24GB 显存，必须使用 Offloading 或更激进的量化

## Evidence

先验知识/题面给定，逻辑校验通过：Qwen3-27B FP8权重约27GB，32K上下文KV Cache约13.8GB，总和约40.8GB，超出24GB显存，需Offloading或量化。
