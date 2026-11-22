# N54: KV Cache 单请求占用量计算实例：假设 L=54, H_kv=8 (GQA), D_h=128, Seq=32768, BF16 (2 bytes)，则 

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N12

## Claim

KV Cache 单请求占用量计算实例：假设 L=54, H_kv=8 (GQA), D_h=128, Seq=32768, BF16 (2 bytes)，则 KV Size = 2 * 54 * 8 * 128 * 32768 * 2 bytes ≈ 7.25 GB；若为 MHA (H_kv=32)，则约为 29 GB，差异巨大

## Corrected Claim

KV Cache 单请求占用量计算实例：假设 L=54, H_kv=8 (GQA), D_h=128, Seq=32768, BF16 (2 bytes)，则 KV Size = 2 * 54 * 8 * 128 * 32768 * 2 bytes ≈ 7.25 GB；若为 MHA (H_kv=32)，则约为 29 GB，差异巨大

## Evidence

先验知识/题面给定，逻辑校验通过：计算过程 2 * 54 * 8 * 128 * 32768 * 2 = 7,247,757,312 bytes ≈ 6.74 GiB (或 7.25 GB 十进制)，MHA 情况为 4 倍即 ≈ 27 GiB (或 29 GB 十进制)，数值量级与逻辑均正确。

## Search Query

Qwen3-27B GQA vs MHA KV cache size calculation 32k context
