# N169: Qwen3-27B 在 FP8 精度下的单卡权重占用修正：若 N54 确认 KV Cache 实际仅 ~4.3GB (非 16GB)，则单卡 24GB 显存下，

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N52

## Claim

Qwen3-27B 在 FP8 精度下的单卡权重占用修正：若 N54 确认 KV Cache 实际仅 ~4.3GB (非 16GB)，则单卡 24GB 显存下，FP8 权重 (27GB) 仍超出容量，必须采用 W4 量化 (权重 ~13.5GB) 或 INT8 (权重 ~27GB，需配合极小 KV) 才能单卡运行；若坚持 2 卡 TP，每卡需加载 13.5GB (W4) 或 27GB (INT8, 不可行) 权重，结合修正后的 KV 分片 (每卡 ~2.15GB)，2x4090 的 W4 方案显存占用为 13.5 + 2.15 + 1.0 (激活值/缓冲) ≈ 16.65GB/卡，满足 24GB 限制，无需 Offloading。

## Corrected Claim

Qwen3-27B 在 FP8 精度下的单卡权重占用修正：若 N54 确认 KV Cache 实际仅 ~4.3GB (非 16GB)，则单卡 24GB 显存下，FP8 权重 (27GB) 仍超出容量，必须采用 W4 量化 (权重 ~13.5GB) 或 INT8 (权重 ~27GB，需配合极小 KV) 才能单卡运行；若坚持 2 卡 TP，每卡需加载 13.5GB (W4) 或 27GB (INT8, 不可行) 权重，结合修正后的 KV 分片 (每卡 ~2.15GB)，2x4090 的 W4 方案显存占用为 13.5 + 2.15 + 1.0 (激活值/缓冲) ≈ 16.65GB/卡，满足 24GB 限制，无需 Offloading。

## Evidence

先验知识/题面给定，逻辑校验通过：FP8权重27GB超出单卡24GB显存，W4量化后权重约13.5GB，加上KV Cache分片(2.15GB)和激活值(1.0GB)，总占用约16.65GB，符合24GB显存限制。

## Search Query

Qwen3-27B AWQ W4 quantization memory footprint 24GB GPU
