# N108: RTX 3090/4090/5090 单卡显存容量 (24GB/24GB/32GB) 与 Qwen3-27B BF16 权重+32K KV Cache 需求 (

- **status**: verified
- **level**: L3
- **source**: given
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N24

## Claim

RTX 3090/4090/5090 单卡显存容量 (24GB/24GB/32GB) 与 Qwen3-27B BF16 权重+32K KV Cache 需求 (55GB) 的缺口量化：3090/4090 缺口 31GB，5090 缺口 23GB，需通过 INT8/FP8 量化或双卡 TP 弥补

## Corrected Claim

RTX 3090/4090/5090 单卡显存容量 (24GB/24GB/32GB) 与 Qwen3-27B BF16 权重+32K KV Cache 需求 (55GB) 的缺口量化：3090/4090 缺口 31GB，5090 缺口 23GB，需通过 INT8/FP8 量化或双卡 TP 弥补

## Evidence

先验知识/题面给定，逻辑校验通过：RTX 3090/4090显存为24GB，5090为32GB；Qwen3-27B BF16权重约54GB，加上32K上下文KV Cache后总需求约55GB，缺口计算（55-24=31, 55-32=23）准确无误。
