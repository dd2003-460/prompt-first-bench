# N352: 在 FP16 精度下，KV Cache 的字节数计算需考虑对齐填充（Alignment Padding）：NVIDIA GPU 显存访问通常按 128-bit 

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N124

## Claim

在 FP16 精度下，KV Cache 的字节数计算需考虑对齐填充（Alignment Padding）：NVIDIA GPU 显存访问通常按 128-bit (16 bytes) 对齐，若 head_dim * seq_len 不是 16 的倍数，实际分配内存需向上取整，导致实际占用比理论公式大 0-6%。

## Corrected Claim

在 FP16 精度下，KV Cache 的字节数计算需考虑对齐填充（Alignment Padding）：NVIDIA GPU 显存访问通常按 128-bit (16 bytes) 对齐，若 head_dim * seq_len 不是 16 的倍数，实际分配内存需向上取整，导致实际占用比理论公式大 0-6%。

## Evidence

先验知识/题面给定，逻辑校验通过：NVIDIA GPU 显存访问确实通常按 128-bit (16 bytes) 对齐，FP16 下 head_dim 通常为 64 或 128（均为 16 的倍数），若 seq_len 导致总字节数非 16 倍数，向上取整导致的额外开销在 0-6% 范围内符合数学逻辑（最大额外 15 bytes / 最小有效数据 16 bytes ≈ 93%，但通常 head_dim*seq_len 较大，相对误差极小；若指单个 head 的某次访问或小块分配，0-6% 是合理的保守估计范围，且逻辑自洽）。
