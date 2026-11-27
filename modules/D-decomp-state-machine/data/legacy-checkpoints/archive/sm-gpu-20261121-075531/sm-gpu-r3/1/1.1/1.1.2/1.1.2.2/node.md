# N135: FP8 量化下，若框架支持 FP8 KV Cache，则 KV Cache 字节数 = 2 * L * n_kv_heads * d_head * seq_le

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N36

## Claim

FP8 量化下，若框架支持 FP8 KV Cache，则 KV Cache 字节数 = 2 * L * n_kv_heads * d_head * seq_len * bytes_per_elem；若 KV Cache 保留 BF16，则 bytes_per_elem=2，导致 32K 上下文下 KV Cache 占用翻倍至约 3.86GB (vs FP8 的 1.93GB)，总显存占用增加 1.93GB。

## Corrected Claim

FP8 量化下，若框架支持 FP8 KV Cache，则 KV Cache 字节数 = 2 * L * n_kv_heads * d_head * seq_len * bytes_per_elem；若 KV Cache 保留 BF16，则 bytes_per_elem=2，导致 32K 上下文下 KV Cache 占用翻倍至约 3.86GB (vs FP8 的 1.93GB)，总显存占用增加 1.93GB。

## Evidence

先验知识/题面给定，逻辑校验通过：公式结构正确（2代表K和V，系数合理），数值计算自洽（1.93GB * 2 = 3.86GB，差值1.93GB），符合FP8(1字节)与BF16(2字节)的存储特性。

## Search Query

FP8 KV cache size calculation LLM inference
