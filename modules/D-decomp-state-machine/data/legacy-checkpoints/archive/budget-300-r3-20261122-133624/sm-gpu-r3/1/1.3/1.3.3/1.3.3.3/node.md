# N200: Prefill 阶段 FlashAttention 算法的中间工作空间 (Workspace) 开销：FlashAttention 需要额外的显存用于存储 so

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N51

## Claim

Prefill 阶段 FlashAttention 算法的中间工作空间 (Workspace) 开销：FlashAttention 需要额外的显存用于存储 softmax 归一化因子和部分注意力矩阵，其大小约为 O(B * L * N_heads) * 4 bytes。对于 Qwen3-27B (N_heads=32), B=1, L=32768，计算得 1 * 32768 * 32 * 4 = 4 MB，结合 N140 的激活缓冲，Prefill 总非 KV 开销在 32K 上下文下通常 < 1 GB，修正 N51 的 1.0-2.0GB 范围上限。

## Corrected Claim

Prefill 阶段 FlashAttention 算法的中间工作空间 (Workspace) 开销：FlashAttention 需要额外的显存用于存储 softmax 归一化因子和部分注意力矩阵，其大小约为 O(B * L * N_heads) * 4 bytes。对于 Qwen3-27B (N_heads=32), B=1, L=32768，计算得 1 * 32768 * 32 * 4 = 4 MB，结合 N140 的激活缓冲，Prefill 总非 KV 开销在 32K 上下文下通常 < 1 GB，修正 N51 的 1.0-2.0GB 范围上限。

## Evidence

先验知识/题面给定，逻辑校验通过：FlashAttention 的 workspace 开销主要取决于序列长度和头数，公式 O(B*L*N_heads)*4 bytes 符合算法原理，数值计算 1*32768*32*4 = 4MB 正确，且该量级远小于 1GB，逻辑自洽。
