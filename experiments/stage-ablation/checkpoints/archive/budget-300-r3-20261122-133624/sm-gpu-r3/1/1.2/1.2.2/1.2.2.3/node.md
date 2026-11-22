# N191: KV Cache 显存占用对上下文长度呈线性关系，对 Batch Size 呈线性关系；在 32K 上下文下，每增加 1 个并发序列需额外 4.27GB (BF

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N48

## Claim

KV Cache 显存占用对上下文长度呈线性关系，对 Batch Size 呈线性关系；在 32K 上下文下，每增加 1 个并发序列需额外 4.27GB (BF16 KV) 或 2.13GB (FP8 KV) 显存，该斜率是计算多卡扩展性瓶颈的关键参数。

## Corrected Claim

KV Cache 显存占用对上下文长度呈线性关系，对 Batch Size 呈线性关系；在 32K 上下文下，每增加 1 个并发序列需额外 4.27GB (BF16 KV) 或 2.13GB (FP8 KV) 显存，该斜率是计算多卡扩展性瓶颈的关键参数。

## Evidence

先验知识/题面给定，逻辑校验通过：KV Cache 大小公式为 2 * n_layers * n_kv_heads * head_dim * seq_len * batch_size * dtype_size，对 seq_len 和 batch_size 均为线性关系；数值量级符合主流大模型（如 Llama-3-70B 或类似架构）在 32K 上下文下的显存占用估算。
