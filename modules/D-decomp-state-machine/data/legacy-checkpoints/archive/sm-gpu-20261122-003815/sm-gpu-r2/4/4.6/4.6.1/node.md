# N135: 多卡Tensor Parallelism中All-Reduce通信数据量量化：每次All-Reduce传输数据量 = Batch_Size * L_seq * 

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N27

## Claim

多卡Tensor Parallelism中All-Reduce通信数据量量化：每次All-Reduce传输数据量 = Batch_Size * L_seq * Hidden_Dim * Bytes_per_element。对于Qwen3-27B (Hidden_Dim=4096, BF16), Batch=1, L_seq=32K, 单层传输量 ≈ 1 * 32768 * 4096 * 2 bytes ≈ 256 MB。

## Corrected Claim

多卡Tensor Parallelism中All-Reduce通信数据量量化：每次All-Reduce传输数据量 = Batch_Size * L_seq * Hidden_Dim * Bytes_per_element。对于Qwen3-27B (Hidden_Dim=4096, BF16), Batch=1, L_seq=32K, 单层传输量 ≈ 1 * 32768 * 4096 * 2 bytes ≈ 256 MB。

## Evidence

先验知识/题面给定，逻辑校验通过：公式 Batch_Size * L_seq * Hidden_Dim * Bytes_per_element 符合 Tensor Parallelism 中 All-Reduce 通信量的基本定义（针对激活值或中间结果），数值计算 1 * 32768 * 4096 * 2 = 268,435,456 bytes = 256 MB 准确无误。
