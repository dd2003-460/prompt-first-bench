# N354: Qwen3-27B 32K 上下文 INT8 KV Cache 显存占用计算：KV_GB = (2 * 64 * 4 * 256 * 32768 * 1) / 

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N110

## Claim

Qwen3-27B 32K 上下文 INT8 KV Cache 显存占用计算：KV_GB = (2 * 64 * 4 * 256 * 32768 * 1) / 1024^3 ≈ 4.0 GB（假设 num_layers=64, num_kv_heads=4, head_dim=256, seq_len=32768, dtype_size=1）

## Corrected Claim

Qwen3-27B 32K 上下文 INT8 KV Cache 显存占用计算：KV_GB = (2 * 64 * 4 * 256 * 32768 * 1) / 1024^3 ≈ 4.0 GB（假设 num_layers=64, num_kv_heads=4, head_dim=256, seq_len=32768, dtype_size=1）

## Evidence

先验知识/题面给定，逻辑校验通过：公式结构正确（2*KV heads*head_dim*seq_len*layers*dtype_size），数值计算 (2*64*4*256*32768*1)/1073741824 ≈ 4.0 准确无误。
