# N182: Qwen3-27B 32K 上下文下的 KV Cache 大小计算公式：KV_Size = 2 (K+V) * n_layers(48) * n_kv_head

- **status**: pending
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

父节点级核验未通过：有冗余（子节点之间存在严重的参数冗余和事实错误。1. 冗余：两个子节点本质上是同一公式在 `dtype_bytes` 参数取不同值（2 vs 1）时的特例，应合并为一个包含变量的通用节点或仅保留公式推导，而非拆分为两个独立的事实节点。2. 错误：父节点声称 Qwen3-27B 有 48 层和 4 个 KV heads，而子节点计算使用了 64 层和 8 个 KV heads。经查证，Qwen3-27B 实际架构为 64 层、8 KV heads（GQA 8:1），子节点的计算参数是正确的，但父节点提供的参数（48层/4头）是错误的，导致父节点结论（3.2GB）与子节点结论（16GB）严重矛盾。虽然子节点之间逻辑一致，但它们与父节点矛盾，且子节点之间因仅差一个系数而高度冗余。）
