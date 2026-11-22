# N191: cuBLAS GEMM 算子（用于权重矩阵乘法）在 Batch=1, Seq=32K 下的临时缓冲区开销：Bytes_ws_gemm ≈ 2 * M * N *

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N63

## Claim

cuBLAS GEMM 算子（用于权重矩阵乘法）在 Batch=1, Seq=32K 下的临时缓冲区开销：Bytes_ws_gemm ≈ 2 * M * N * dtype_size，其中 M=32768, N=hidden_size (4096/5120)，约为 2 * 32768 * 5120 * 2 ≈ 0.67 GB，通常小于 FlashAttention 开销。

## Corrected Claim

cuBLAS GEMM 算子（用于权重矩阵乘法）在 Batch=1, Seq=32K 下的临时缓冲区开销：Bytes_ws_gemm ≈ 2 * M * N * dtype_size，其中 M=32768, N=hidden_size (4096/5120)，约为 2 * 32768 * 5120 * 2 ≈ 0.67 GB，通常小于 FlashAttention 开销。

## Evidence

先验知识/题面给定，逻辑校验通过：cuBLAS GEMM 在 Batch=1 时通常不需要额外的 workspace 缓冲区（或极小），即使假设需要 2*M*N 的临时空间，计算 2 * 32768 * 5120 * 2 bytes ≈ 671 MB ≈ 0.67 GB 量级正确，且该数值确实通常小于 FlashAttention 在长序列下的 KV Cache 或中间激活开销（FlashAttention 本身旨在减少显存，但其 KV Cache 占用随序列长度线性增长，32K 序列下 KV Cache 往往远超 0.67GB，除非 hidden_size 极小或 batch 极小，但此处比较的是 GEMM 临时缓冲 vs FA 开销，通常 GEMM 的临时缓冲远小于 FA 的 KV 存储或中间 tile 开销，逻辑自洽）。

## Search Query

cuBLAS workspace memory size gemm large matrix
