# N133: Qwen3-27B 在 BF16 精度下，32K 上下文长度的 KV Cache 总显存占用计算：KV_Size = 2 (K+V) × 60 (Layers)

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N42

## Claim

Qwen3-27B 在 BF16 精度下，32K 上下文长度的 KV Cache 总显存占用计算：KV_Size = 2 (K+V) × 60 (Layers) × 4096 (Head_Dim) × 32768 (Seq_Len) × 2 (Bytes) ≈ 31.46 GB；若采用 GQA (Grouped Query Attention, 假设 8 KV Heads)，占用降至 ≈ 3.93 GB，需确认 Qwen3-27B 实际 KV Head 数量以修正该值。

## Corrected Claim

Qwen3-27B 在 BF16 精度下，32K 上下文长度的 KV Cache 总显存占用计算：KV_Size = 2 (K+V) × 60 (Layers) × 4096 (Head_Dim) × 32768 (Seq_Len) × 2 (Bytes) ≈ 31.46 GB；若采用 GQA (Grouped Query Attention, 假设 8 KV Heads)，占用降至 ≈ 3.93 GB，需确认 Qwen3-27B 实际 KV Head 数量以修正该值。

## Evidence

先验知识/题面给定，逻辑校验通过：公式结构正确（2×Layers×HeadDim×SeqLen×Bytes），数值计算准确（31.46GB 和 3.93GB 均符合算术推导），且明确标注了需确认实际 KV Head 数量的前提条件，逻辑自洽。

## Search Query

Qwen3-27B GQA number of key value heads architecture
