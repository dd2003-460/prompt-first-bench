# N184: KV Cache显存随上下文长度线性增长公式验证：KV_Bytes = 2 * n_layers * n_kv_heads * head_dim * dtype

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N56

## Claim

KV Cache显存随上下文长度线性增长公式验证：KV_Bytes = 2 * n_layers * n_kv_heads * head_dim * dtype_size * seq_len。对于Qwen3-27B (假设64层, 8 KV头, 128维)，每增加1000 tokens，BF16 KV Cache增加 256 MB。32K上下文下总KV Cache为 8 GB (BF16) 或 4 GB (FP8)，而非N56所述的25.77 GB。

## Corrected Claim

KV Cache显存随上下文长度线性增长公式验证：KV_Bytes = 2 * n_layers * n_kv_heads * head_dim * dtype_size * seq_len。对于Qwen3-27B (假设64层, 8 KV头, 128维)，每增加1000 tokens，BF16 KV Cache增加 256 MB。32K上下文下总KV Cache为 8 GB (BF16) 或 4 GB (FP8)，而非N56所述的25.77 GB。

## Evidence

先验知识/题面给定，逻辑校验通过：公式推导正确，数值计算（256MB/1000 tokens, 8GB/32K）与假设参数一致

## Search Query

LLM KV cache memory linear growth formula
