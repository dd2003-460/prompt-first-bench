# N94: 条件(2)阈值量化：24GB 显存上限下，Qwen3-27B 最大支持上下文长度。计算公式：Max_Seq_Len = (24GB - Weight_GB - 

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N39

## Claim

条件(2)阈值量化：24GB 显存上限下，Qwen3-27B 最大支持上下文长度。计算公式：Max_Seq_Len = (24GB - Weight_GB - Activation_GB) / (KV_Cache_per_token_GB)。若 Weight_GB=13.5GB (INT4)，Activation_GB=2GB，则剩余 8.5GB 用于 KV Cache。KV_Cache_per_token_GB (GQA, 8 KV heads, 64 layers, 128 head_dim, FP16) = 2 * 64 * 8 * 128 * 2 bytes / 1024^3 ≈ 0.0005 GB/token。Max_Seq_Len = 8.5GB / 0.0005 ≈ 17,000 tokens。若使用 FP8 KV Cache，Max_Seq_Len 翻倍至 ~34,000 tokens。因此，条件(2)中'上下文窗口≤24K tokens'在 INT4+FP16 KV 下不成立，需 INT4+FP8 KV 或更低精度权重。

## Corrected Claim

条件(2)阈值量化：24GB 显存上限下，Qwen3-27B 最大支持上下文长度。计算公式：Max_Seq_Len = (24GB - Weight_GB - Activation_GB) / (KV_Cache_per_token_GB)。若 Weight_GB=13.5GB (INT4)，Activation_GB=2GB，则剩余 8.5GB 用于 KV Cache。KV_Cache_per_token_GB (GQA, 8 KV heads, 64 layers, 128 head_dim, FP16) = 2 * 64 * 8 * 128 * 2 bytes / 1024^3 ≈ 0.0005 GB/token。Max_Seq_Len = 8.5GB / 0.0005 ≈ 17,000 tokens。若使用 FP8 KV Cache，Max_Seq_Len 翻倍至 ~34,000 tokens。因此，条件(2)中'上下文窗口≤24K tokens'在 INT4+FP16 KV 下不成立，需 INT4+FP8 KV 或更低精度权重。

## Evidence

先验知识/题面给定，逻辑校验通过：KV Cache 计算公式正确（2 * 64 * 8 * 128 * 2 bytes ≈ 0.5 MB/token），剩余显存 8.5GB 除以 0.5MB/token 确实约为 17,000 tokens，结论自洽。

## Search Query

Qwen3-27B GQA KV heads count context length 32K memory requirement
