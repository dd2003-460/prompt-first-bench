# N300: FlashAttention-2 优化后的激活值显存占用：通过将注意力矩阵分块计算，峰值激活显存降低至 O(N) 而非 O(N^2)，对于 32K 序列，实际瞬

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N104, N105, N106

## Claim

FlashAttention-2 优化后的激活值显存占用：通过将注意力矩阵分块计算，峰值激活显存降低至 O(N) 而非 O(N^2)，对于 32K 序列，实际瞬时占用通常 <2 GB (主要为 QKV 投影和输出投影的中间结果)，N105 中 2-4GB 的估计在 FlashAttention 下是合理的上界

## Corrected Claim

FlashAttention-2 优化后的激活值显存占用：通过将注意力矩阵分块计算，峰值激活显存降低至 O(N) 而非 O(N^2)，对于 32K 序列，实际瞬时占用通常 <2 GB (主要为 QKV 投影和输出投影的中间结果)，N105 中 2-4GB 的估计在 FlashAttention 下是合理的上界

## Evidence

先验知识/题面给定，逻辑校验通过：FlashAttention-2 通过分块计算避免存储完整的 N×N 注意力矩阵，将激活显存复杂度从 O(N^2) 降至 O(N)；对于 32K 序列，O(N) 级别的中间结果（如 QKV 投影、输出投影等）显存占用通常在 2GB 以内，2-4GB 作为上界估计合理。

## Search Query

FlashAttention memory usage LLM inference 32k context
