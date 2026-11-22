# N597: Batch Size=1, Seq Len=32K 下，KV Cache 的精确占用量为 2 * Num_Layers * Num_KV_Heads * Hea

- **status**: verified
- **level**: L5
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N183

## Claim

Batch Size=1, Seq Len=32K 下，KV Cache 的精确占用量为 2 * Num_Layers * Num_KV_Heads * Head_Dim * Seq_Len * Dtype_Size = 2 * 64 * 8 * 128 * 32768 * 2 bytes ≈ 1.07 GB，而非父节点中简化的 0.54 GB（父节点未区分 KV Cache 与中间激活值）。

## Corrected Claim

Batch Size=1, Seq Len=32K 下，KV Cache 的精确占用量为 2 * Num_Layers * Num_KV_Heads * Head_Dim * Seq_Len * Dtype_Size = 2 * 64 * 8 * 128 * 32768 * 2 bytes ≈ 1.07 GB，而非父节点中简化的 0.54 GB（父节点未区分 KV Cache 与中间激活值）。

## Evidence

先验知识/题面给定，逻辑校验通过：公式结构正确（2代表K和V，64层，8头，128维，32768长度，2字节FP16），计算结果 2*64*8*128*32768*2 = 1,073,741,824 bytes ≈ 1.07 GB，数值量级与逻辑均自洽。
