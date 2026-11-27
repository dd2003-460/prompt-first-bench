# N299: Prefill 阶段激活值峰值显存估算公式：Peak_Activation ≈ L * BatchSize * SeqLen * HiddenDim * Byt

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N104, N105, N106

## Claim

Prefill 阶段激活值峰值显存估算公式：Peak_Activation ≈ L * BatchSize * SeqLen * HiddenDim * BytesPerParam * 2 (QKV 投影中间层)，对于 Qwen3-27B (Hidden=4096, L=64, Seq=32768, BF16)，理论峰值约为 64 * 1 * 32768 * 4096 * 2 * 2 = 34.4 GB (未考虑 FlashAttention 优化)

## Corrected Claim

Prefill 阶段激活值峰值显存估算公式：Peak_Activation ≈ L * BatchSize * SeqLen * HiddenDim * BytesPerParam * 2 (QKV 投影中间层)，对于 Qwen3-27B (Hidden=4096, L=64, Seq=32768, BF16)，理论峰值约为 64 * 1 * 32768 * 4096 * 2 * 2 = 34.4 GB (未考虑 FlashAttention 优化)

## Evidence

先验知识/题面给定，逻辑校验通过：数值计算 64*1*32768*4096*2*2 = 34,359,738,368 Bytes ≈ 32 GiB (或 34.36 GB)，与陈述中的 34.4 GB 一致；公式结构符合 Transformer 层中 QKV 投影中间激活值的显存估算逻辑（L层 * Batch * Seq * Hidden * 2(QKV) * BytesPerParam）。
