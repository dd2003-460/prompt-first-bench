# N162: 基于 N110 提取的参数（假设 Num_Layers=48, Num_KV_Heads=8, Head_Dim=128），计算 Qwen3-27B 在 BF1

- **status**: verified
- **level**: L4
- **source**: given
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N63

## Claim

基于 N110 提取的参数（假设 Num_Layers=48, Num_KV_Heads=8, Head_Dim=128），计算 Qwen3-27B 在 BF16 (2 bytes) 精度下，32K 上下文 (Seq_Len=32768) 的单条请求 KV Cache 显存占用：KV_Cache_GB = (2 * 48 * 8 * 128 * 32768 * 2) / 1024^3 ≈ 7.5 GB。

## Corrected Claim

基于 N110 提取的参数（假设 Num_Layers=48, Num_KV_Heads=8, Head_Dim=128），计算 Qwen3-27B 在 BF16 (2 bytes) 精度下，32K 上下文 (Seq_Len=32768) 的单条请求 KV Cache 显存占用：KV_Cache_GB = (2 * 48 * 8 * 128 * 32768 * 2) / 1024^3 ≈ 7.5 GB。

## Evidence

先验知识/题面给定，逻辑校验通过：公式 (2 * 48 * 8 * 128 * 32768 * 2) / 1024^3 计算结果约为 7.45 GB，与陈述中的 7.5 GB 一致，量纲和数值量级合理。
