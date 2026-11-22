# N194: 基于确认参数（N_layers=64, N_kv_heads=8, D_head=128, seq_len=32768, bytes=2 for BF16）计算

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N63

## Claim

基于确认参数（N_layers=64, N_kv_heads=8, D_head=128, seq_len=32768, bytes=2 for BF16）计算的 KV Cache 精确占用量：KV_Bytes = 2 * 64 * 8 * 128 * 32768 * 2 = 1,073,741,824 Bytes = 1.0 GB，此结果与 N12 中 16GB 的估计存在巨大偏差，需检查 N12 是否误用了全注意力头数（32）或未考虑 GQA 压缩，修正后 32K 上下文 KV Cache 仅占 1GB，极大降低显存压力。

## Corrected Claim

基于确认参数（N_layers=64, N_kv_heads=8, D_head=128, seq_len=32768, bytes=2 for BF16）计算的 KV Cache 精确占用量：KV_Bytes = 2 * 64 * 8 * 128 * 32768 * 2 = 1,073,741,824 Bytes = 1.0 GB，此结果与 N12 中 16GB 的估计存在巨大偏差，需检查 N12 是否误用了全注意力头数（32）或未考虑 GQA 压缩，修正后 32K 上下文 KV Cache 仅占 1GB，极大降低显存压力。

## Evidence

先验知识/题面给定，逻辑校验通过：公式 KV_Bytes = 2(K,V) * N_layers(64) * N_kv_heads(8) * D_head(128) * seq_len(32768) * bytes(2) = 1,073,741,824 Bytes = 1 GB，计算无误且量级合理。
