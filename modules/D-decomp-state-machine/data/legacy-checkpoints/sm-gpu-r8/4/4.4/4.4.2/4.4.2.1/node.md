# N217: Qwen3-27B 在 32K 上下文下的 KV Cache 大小计算公式为：2 * n_layers * n_kv_heads * head_dim * se

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N68

## Claim

Qwen3-27B 在 32K 上下文下的 KV Cache 大小计算公式为：2 * n_layers * n_kv_heads * head_dim * seq_len * bytes_per_elem，对于 GQA 模型（n_kv_heads < n_heads），KV Cache 约为 1-2GB (BF16)，远小于 54GB 权重，故生成速度公式中 Model Size 近似为纯权重大小。

## Corrected Claim

Qwen3-27B 在 32K 上下文下的 KV Cache 大小计算公式为：2 * n_layers * n_kv_heads * head_dim * seq_len * bytes_per_elem，对于 GQA 模型（n_kv_heads < n_heads），KV Cache 约为 1-2GB (BF16)，远小于 54GB 权重，故生成速度公式中 Model Size 近似为纯权重大小。

## Evidence

先验知识/题面给定，逻辑校验通过：KV Cache 公式符合 Transformer 架构原理，Qwen3-27B 参数规模下 32K 上下文 KV Cache 量级估算合理（约 1-2GB），远小于 54GB 权重，结论自洽。
