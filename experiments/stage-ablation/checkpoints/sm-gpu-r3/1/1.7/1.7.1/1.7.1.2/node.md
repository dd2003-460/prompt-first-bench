# N182: Qwen3-27B 32K 上下文下的 KV Cache 大小计算公式：KV_Size = 2 (K+V) * n_layers(48) * n_kv_head

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N92

## Claim

Qwen3-27B 32K 上下文下的 KV Cache 大小计算公式：KV_Size = 2 (K+V) * n_layers(48) * n_kv_heads(4) * head_dim(128) * seq_len(32768) * dtype_bytes；若 KV Cache 保持 BF16 (2 bytes)，则 KV_Size ≈ 3.2 GB；若 KV Cache 也量化为 FP8 (1 byte)，则 KV_Size ≈ 1.6 GB。

## Corrected Claim

Qwen3-27B 32K 上下文下的 KV Cache 大小计算公式：KV_Size = 2 (K+V) * n_layers(48) * n_kv_heads(4) * head_dim(128) * seq_len(32768) * dtype_bytes；若 KV Cache 保持 BF16 (2 bytes)，则 KV_Size ≈ 3.2 GB；若 KV Cache 也量化为 FP8 (1 byte)，则 KV_Size ≈ 1.6 GB。

## Evidence

先验知识/题面给定，逻辑校验通过：Qwen3-27B 架构参数（48层, 4 KV头, 128维）符合 GQA 设计，数值计算 2*48*4*128*32768*2 ≈ 3.22GB 与 1.61GB 准确无误。
