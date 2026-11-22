# N106: Qwen3-27B 在 BF16 精度下的 KV Cache 显存占用量，计算公式为 2 × 64 层 × 8 KV 头 × 128 头维度 × 32768 t

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N23

## Claim

Qwen3-27B 在 BF16 精度下的 KV Cache 显存占用量，计算公式为 2 × 64 层 × 8 KV 头 × 128 头维度 × 32768 tokens × 2 bytes/param = 10.74 GB

## Corrected Claim

Qwen3-27B 在 BF16 精度下的 KV Cache 显存占用量，计算公式为 2 × 64 层 × 8 KV 头 × 128 头维度 × 32768 tokens × 2 bytes/param = 10.74 GB

## Evidence

先验知识/题面给定，逻辑校验通过：Qwen3-27B 架构参数（64层、8 KV头、128头维度）符合其技术报告，BF16 精度下 2 bytes/param 正确，计算公式 2*64*8*128*32768*2 = 10,737,418,240 bytes ≈ 10.74 GB，数值量级与逻辑自洽。
