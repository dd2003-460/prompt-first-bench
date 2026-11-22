# N458: 32K 上下文 KV Cache 显存占用精确计算：基于 N8 公式，假设 Qwen3-27B 有 64 层，head_dim=128，num_kv_heads

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N150

## Claim

32K 上下文 KV Cache 显存占用精确计算：基于 N8 公式，假设 Qwen3-27B 有 64 层，head_dim=128，num_kv_heads=8 (GQA)，seq_len=32768。KV Cache Size = 2 (K+V) × 64 (layers) × 8 (kv_heads) × 128 (head_dim) × 32768 (seq) × 2 (bytes, BF16) ≈ 8.5 GB。若 FP8 则为 ~4.3 GB。

## Corrected Claim

32K 上下文 KV Cache 显存占用精确计算：基于 N8 公式，假设 Qwen3-27B 有 64 层，head_dim=128，num_kv_heads=8 (GQA)，seq_len=32768。KV Cache Size = 2 (K+V) × 64 (layers) × 8 (kv_heads) × 128 (head_dim) × 32768 (seq) × 2 (bytes, BF16) ≈ 8.5 GB。若 FP8 则为 ~4.3 GB。

## Evidence

先验知识/题面给定，逻辑校验通过：计算过程 2×64×8×128×32768×2 = 8,589,934,592 bytes ≈ 8.59 GB，与陈述一致；FP8 减半约为 4.3 GB，逻辑自洽。

## Search Query

LLM KV cache memory calculation formula GQA layers heads
