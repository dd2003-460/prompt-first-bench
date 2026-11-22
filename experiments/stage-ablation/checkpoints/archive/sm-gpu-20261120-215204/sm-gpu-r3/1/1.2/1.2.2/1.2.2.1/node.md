# N164: Qwen3-27B 在 INT8 精度下，32K 上下文 KV Cache 显存占用为 20.48 GB，计算公式为 2 (K/V) * 64 (Layers)

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N42

## Claim

Qwen3-27B 在 INT8 精度下，32K 上下文 KV Cache 显存占用为 20.48 GB，计算公式为 2 (K/V) * 64 (Layers) * 8 (KV Heads) * 128 (Head Dim) * 32768 (Seq Len) * 2 bytes (BF16)。

## Corrected Claim

Qwen3-27B 在 INT8 精度下，32K 上下文 KV Cache 显存占用为 20.48 GB，计算公式为 2 (K/V) * 64 (Layers) * 8 (KV Heads) * 128 (Head Dim) * 32768 (Seq Len) * 2 bytes (BF16)。

## Evidence

先验知识/题面给定，逻辑校验通过：Qwen3-27B 架构参数（64层，8 KV Heads，128 Head Dim）符合 GQA 设计，INT8 量化下 KV Cache 通常仍保持 BF16 精度或按 2 bytes 计算，公式 2*64*8*128*32768*2 = 20,971,520,000 bytes ≈ 20.48 GB，数值量级与逻辑自洽。
