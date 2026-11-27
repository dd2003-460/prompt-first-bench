# N691: llama.cpp 中 KV Cache 索引结构 (Slot IDs) 的内存开销计算公式为 Seq_Len * n_kv_heads * head_dim 

- **status**: degraded
- **level**: L5
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N247

## Claim

llama.cpp 中 KV Cache 索引结构 (Slot IDs) 的内存开销计算公式为 Seq_Len * n_kv_heads * head_dim * 4 bytes，对于 32K 上下文、n_kv_heads=8、head_dim=128，该值为 32768 * 8 * 128 * 4 = 134,217,728 bytes = 128 MB。

## Corrected Claim

llama.cpp 中 KV Cache 数据体（Key 和 Value 向量）的内存开销计算公式通常为 2 * Seq_Len * n_kv_heads * head_dim * dtype_size。对于 32K 上下文、n_kv_heads=8、head_dim=128 且使用 float16 (2 bytes) 时，该值为 2 * 32768 * 8 * 128 * 2 = 134,217,728 bytes = 128 MB。

## Evidence

[质询]概念混淆与量级错误：KV Cache 存储的是 Key 和 Value 的向量（float16/float32），而非 'Slot IDs'（索引/整数）。Slot IDs 通常仅为整数索引，内存开销极小（如 4 bytes/seq），不可能达到 128MB。此外，128MB 是 KV Cache 数据本身的典型大小（32K * 8 * 128 * 2 bytes * 2(K&V) = 128MB 若用 fp16，或 256MB 若用 fp32），但将其称为 'Slot IDs 的内存开销' 是严重的术语和逻辑错误。 | 逻辑校验失败：'Slot IDs' 指代索引结构，其内存占用应为 O(Seq_Len) 的整数数组，而非 O(Seq_Len * Heads * Dim) 的浮点张量。陈述将 KV Cache 数据体的大小错误地归因于索引结构，且未区分 K/V 双份存储或数据类型（fp16/fp32），导致概念与数值不匹配。
