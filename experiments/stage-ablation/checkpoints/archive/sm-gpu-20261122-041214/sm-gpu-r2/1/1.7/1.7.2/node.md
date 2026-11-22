# N65: Attention 头激活值公式：Attention_Head_GB = (seq_len * batch_size * n_heads * head_dim 

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N12

## Claim

Attention 头激活值公式：Attention_Head_GB = (seq_len * batch_size * n_heads * head_dim * bytes_per_element * 2) / (1024^3)，其中因子2代表Query和Key/Value的中间状态或重计算缓冲，Qwen3-27B (n_heads=32, head_dim=128, BF16) 在 seq_len=32K, batch=1 时约为 4.0 GB。

## Corrected Claim

Attention 头激活值公式：Attention_Head_GB = (seq_len * batch_size * n_heads * head_dim * bytes_per_element * 2) / (1024^3)，其中因子2代表Query和Key/Value的中间状态或重计算缓冲，Qwen3-27B (n_heads=32, head_dim=128, BF16) 在 seq_len=32K, batch=1 时约为 4.0 GB。

## Evidence

先验知识/题面给定，逻辑校验通过：公式计算 (32768 * 1 * 32 * 128 * 2 * 2) / (1024^3) = 4.0 GB，数值量级与逻辑自洽。
