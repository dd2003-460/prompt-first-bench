# N142: 修正 N40 计算错误：BF16 精度下 32K 上下文 KV Cache 大小 = 2 (K/V) * 64 (L) * 4 (H_kv) * 128 (he

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N40

## Claim

修正 N40 计算错误：BF16 精度下 32K 上下文 KV Cache 大小 = 2 (K/V) * 64 (L) * 4 (H_kv) * 128 (head_dim) * 32768 (seq_len) * 2 (bytes) = 4,294,967,296 bytes ≈ 4.0 GB，原 claim 中的 1.25 GB 错误源于漏乘 K/V 因子或层数/头数错误，此处确认 4.0 GB 为正确值

## Corrected Claim

修正 N40 计算错误：BF16 精度下 32K 上下文 KV Cache 大小 = 2 (K/V) * 64 (L) * 4 (H_kv) * 128 (head_dim) * 32768 (seq_len) * 2 (bytes) = 4,294,967,296 bytes ≈ 4.0 GB，原 claim 中的 1.25 GB 错误源于漏乘 K/V 因子或层数/头数错误，此处确认 4.0 GB 为正确值

## Evidence

先验知识/题面给定，逻辑校验通过：2*64*4*128*32768*2 = 4,294,967,296 bytes ≈ 4.0 GB，计算无误
