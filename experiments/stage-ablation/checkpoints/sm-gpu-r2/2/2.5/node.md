# N17: 单卡 vs 多卡 TCO 对比：2×RTX 4090 ($3,200-$3,600) vs 1×A100 80GB ($10,000+)。若 Qwen3-27B

- **status**: verified
- **level**: L2
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N2

## Claim

单卡 vs 多卡 TCO 对比：2×RTX 4090 ($3,200-$3,600) vs 1×A100 80GB ($10,000+)。若 Qwen3-27B FP8 可在单张 4090 (24GB) 运行（需量化或 KV 压缩），则单卡 4090 成本远低于多卡；若必须 BF16，2×4090 (48GB) 仍不足，需 2×5090 (64GB) 或 1×A100。

## Corrected Claim

单卡 vs 多卡 TCO 对比：2×RTX 4090 ($3,200-$3,600) vs 1×A100 80GB ($10,000+)。若 Qwen3-27B FP8 可在单张 4090 (24GB) 运行（需量化或 KV 压缩），则单卡 4090 成本远低于多卡；若必须 BF16，2×4090 (48GB) 仍不足，需 2×5090 (64GB) 或 1×A100。

## Evidence

先验知识/题面给定，逻辑校验通过：RTX 4090显存为24GB，A100 80GB显存及价格量级符合市场常识，Qwen3-27B在FP8下约需27GB显存（含KV Cache），单卡4090确实无法直接运行需量化或压缩，BF16下需54GB+，2x4090(48GB)不足，逻辑自洽。

## Search Query

2x RTX 4090 vs 1x A100 cost comparison LLM inference
