# N95: KV Cache 显存占用精确计算：KV_Cache_Size = 2 * L * H_kv * D_head * Seq_Len * Bytes_per_to

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N16

## Claim

KV Cache 显存占用精确计算：KV_Cache_Size = 2 * L * H_kv * D_head * Seq_Len * Bytes_per_token。对于 32K 上下文 (Seq_Len=32768)，若 L=64, H_kv=8, D_head=128：BF16 (2 bytes) = 2 * 64 * 8 * 128 * 32768 * 2 = 8.6 GB; FP8/INT8 (1 byte) = 4.3 GB; INT4 (0.5 byte) = 2.15 GB。

## Corrected Claim

KV Cache 显存占用精确计算：KV_Cache_Size = 2 * L * H_kv * D_head * Seq_Len * Bytes_per_token。对于 32K 上下文 (Seq_Len=32768)，若 L=64, H_kv=8, D_head=128：BF16 (2 bytes) = 2 * 64 * 8 * 128 * 32768 * 2 = 8.6 GB; FP8/INT8 (1 byte) = 4.3 GB; INT4 (0.5 byte) = 2.15 GB。

## Evidence

先验知识/题面给定，逻辑校验通过：公式结构正确（2代表K和V，L为层数，H_kv为KV头数，D_head为头维度，Seq_Len为序列长度，Bytes为精度字节数）；数值计算准确（2*64*8*128*32768*2 = 8,589,934,592 bytes ≈ 8.0 GiB，通常工程上近似为8.6 GB或8.59 GB，量级与逻辑均合理；FP8/INT4数值按比例缩放正确）。
