# N10: 32K 上下文长度下 Qwen3-27B 的 KV Cache 显存占用计算公式为：KV_Cache_GB = 2 * Layers * Num_Heads *

- **status**: verified
- **level**: L2
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N1, N2, N3

## Claim

32K 上下文长度下 Qwen3-27B 的 KV Cache 显存占用计算公式为：KV_Cache_GB = 2 * Layers * Num_Heads * Head_Dim * Seq_Len * Bytes_per_KV_Element * Batch_Size。

## Corrected Claim

32K 上下文长度下 Qwen3-27B 的 KV Cache 显存占用计算公式为：KV_Cache_GB = 2 * Layers * Num_Heads * Head_Dim * Seq_Len * Bytes_per_KV_Element * Batch_Size。

## Evidence

先验知识/题面给定，逻辑校验通过：公式结构符合 Transformer KV Cache 显存计算标准（2代表K和V，Layers/Heads/Dim/SeqLen/Bytes/Batch均为标准参数），量纲与逻辑自洽。
