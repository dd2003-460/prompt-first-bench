# N179: BF16 精度下 32K 上下文 KV Cache 显存占用精确计算：2 (K+V) × num_layers (64) × num_kv_heads (8, 

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N42

## Claim

BF16 精度下 32K 上下文 KV Cache 显存占用精确计算：2 (K+V) × num_layers (64) × num_kv_heads (8, GQA) × head_dim (128) × seq_len (32768) × 2 bytes (BF16) = 8.59 GB。注：若模型使用 MQA (Multi-Query Attention, num_kv_heads=1)，则占用降至 1.07 GB；若使用 MHA (num_kv_heads=num_heads=32)，则占用升至 34.36 GB。需确认 Qwen3-27B 具体注意力头配置。

## Corrected Claim

BF16 精度下 32K 上下文 KV Cache 显存占用精确计算：2 (K+V) × num_layers (64) × num_kv_heads (8, GQA) × head_dim (128) × seq_len (32768) × 2 bytes (BF16) = 8.59 GB。注：若模型使用 MQA (Multi-Query Attention, num_kv_heads=1)，则占用降至 1.07 GB；若使用 MHA (num_kv_heads=num_heads=32)，则占用升至 34.36 GB。需确认 Qwen3-27B 具体注意力头配置。

## Evidence

先验知识/题面给定，逻辑校验通过：公式 2×64×8×128×32768×2 计算结果约为 8.59 GB，量级与逻辑自洽。

## Search Query

Qwen3-27B attention heads configuration GQA MQA
