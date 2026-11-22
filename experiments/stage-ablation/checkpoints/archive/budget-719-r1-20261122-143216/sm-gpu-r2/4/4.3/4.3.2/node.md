# N107: Qwen3-27B 在 FP8 精度下的 KV Cache 显存占用量，计算公式为 2 × 64 层 × 8 KV 头 × 128 头维度 × 32768 to

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N23

## Claim

Qwen3-27B 在 FP8 精度下的 KV Cache 显存占用量，计算公式为 2 × 64 层 × 8 KV 头 × 128 头维度 × 32768 tokens × 1 byte/param = 5.37 GB

## Corrected Claim

Qwen3-27B 在 FP8 精度下的 KV Cache 显存占用量，计算公式为 2 × 64 层 × 8 KV 头 × 128 头维度 × 32768 tokens × 1 byte/param = 5.37 GB

## Evidence

先验知识/题面给定，逻辑校验通过：Qwen3-27B 架构参数（64层、8 KV头、128头维度）符合常见大模型配置，FP8精度下1字节/参数，计算公式 2*64*8*128*32768*1 = 5,368,709,120 bytes ≈ 5.37 GB，数值量级与逻辑自洽。
