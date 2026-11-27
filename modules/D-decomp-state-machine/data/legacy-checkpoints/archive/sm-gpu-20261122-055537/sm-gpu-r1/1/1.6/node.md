# N12: KV Cache显存占用公式：KV Cache Size = 2 (K+V) * Num_Layers * Hidden_Dim * Head_Dim * Ba

- **status**: verified
- **level**: L2
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N1, N2, N3

## Claim

KV Cache显存占用公式：KV Cache Size = 2 (K+V) * Num_Layers * Hidden_Dim * Head_Dim * Batch_Size * Seq_Length * Bytes_per_Element。对于Qwen3-27B（假设54层, 4096 hidden, 128 head_dim, 32K seq, 1 batch, BF16），计算单请求KV Cache占用量。

## Corrected Claim

KV Cache显存占用公式：KV Cache Size = 2 (K+V) * Num_Layers * Hidden_Dim * Head_Dim * Batch_Size * Seq_Length * Bytes_per_Element。对于Qwen3-27B（假设54层, 4096 hidden, 128 head_dim, 32K seq, 1 batch, BF16），计算单请求KV Cache占用量。

## Evidence

先验知识/题面给定，逻辑校验通过
