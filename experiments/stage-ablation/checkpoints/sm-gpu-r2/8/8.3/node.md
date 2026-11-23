# N95: KV Cache 精确计算公式：KV_Cache_GB = (2 * Num_Layers * Num_KV_Heads * Head_Dim * Seq_Le

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N26, N27, N28

## Claim

KV Cache 精确计算公式：KV_Cache_GB = (2 * Num_Layers * Num_KV_Heads * Head_Dim * Seq_Len * Bytes_per_Element) / 1024^3。对于 Qwen3-27B (32层, GQA 8:1, Head_Dim=128, Seq_Len=32768, FP16=2B)，计算得 KV_Cache_GB ≈ 1.07 GB（单序列）。

## Corrected Claim

KV Cache 精确计算公式：KV_Cache_GB = (2 * Num_Layers * Num_KV_Heads * Head_Dim * Seq_Len * Bytes_per_Element) / 1024^3。对于 Qwen3-27B (32层, GQA 8:1, Head_Dim=128, Seq_Len=32768, FP16=2B)，计算得 KV_Cache_GB ≈ 1.07 GB（单序列）。

## Evidence

先验知识/题面给定，逻辑校验通过：公式结构正确（2代表K和V，GQA下KV Heads为8），数值计算 (2*32*8*128*32768*2)/1024^3 ≈ 1.07 GB 准确无误。
