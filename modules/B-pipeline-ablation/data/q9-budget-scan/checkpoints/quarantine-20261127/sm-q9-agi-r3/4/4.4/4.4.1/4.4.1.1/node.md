# N205: Llama-3-8B (FP16) 在 V100 (16GB) 上无法运行的量化依据：权重大小 = 8e9 * 2 bytes = 16 GB；V100 显存 

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N72

## Claim

Llama-3-8B (FP16) 在 V100 (16GB) 上无法运行的量化依据：权重大小 = 8e9 * 2 bytes = 16 GB；V100 显存 16 GB；剩余显存 16 - 16 = 0 GB < KV Cache 最小需求 (约 0.1 GB for short seq)，故 OOM。

## Corrected Claim

Llama-3-8B (FP16) 在 V100 (16GB) 上无法运行的量化依据：权重大小 = 8e9 * 2 bytes = 16 GB；V100 显存 16 GB；剩余显存 16 - 16 = 0 GB < KV Cache 最小需求 (约 0.1 GB for short seq)，故 OOM。

## Evidence

先验知识/题面给定，逻辑校验通过：Llama-3-8B参数量约80亿，FP16下权重占用16GB，V100显存16GB，扣除权重后无剩余空间供KV Cache及激活值使用，必然OOM。
