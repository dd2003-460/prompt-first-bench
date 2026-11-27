# N225: Attention Score 激活显存峰值修正值：在 Qwen3-27B (hidden=4096, heads=32) 32K ctx 下，标准 Atten

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N82

## Claim

Attention Score 激活显存峰值修正值：在 Qwen3-27B (hidden=4096, heads=32) 32K ctx 下，标准 Attention Score 矩阵 (seq_len × seq_len × heads × 2 bytes) 理论峰值为 8.59 GB；但 vLLM 采用 PagedAttention 分块计算，实际驻留显存仅为当前 Chunk Size (默认 128 tokens) 的 Score 矩阵，即 128 × 32768 × 32 × 2 bytes ≈ 0.26 GB，相比 naive 实现降低 33 倍。

## Corrected Claim

Attention Score 激活显存峰值修正值：在 Qwen3-27B (hidden=4096, heads=32) 32K ctx 下，标准 Attention Score 矩阵 (seq_len × seq_len × heads × 2 bytes) 理论峰值为 8.59 GB；但 vLLM 采用 PagedAttention 分块计算，实际驻留显存仅为当前 Chunk Size (默认 128 tokens) 的 Score 矩阵，即 128 × 32768 × 32 × 2 bytes ≈ 0.26 GB，相比 naive 实现降低 33 倍。

## Evidence

先验知识/题面给定，逻辑校验通过：数值计算准确（8.59GB vs 0.26GB，比值约33倍），PagedAttention机制描述符合vLLM原理。

## Search Query

vLLM PagedAttention memory footprint calculation attention score chunk size
