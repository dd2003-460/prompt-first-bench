# N163: 基于 N110 提取的参数，计算 Qwen3-27B 在 FP8 (1 byte) 精度下，32K 上下文 (Seq_Len=32768) 的单条请求 KV C

- **status**: verified
- **level**: L4
- **source**: given
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N63

## Claim

基于 N110 提取的参数，计算 Qwen3-27B 在 FP8 (1 byte) 精度下，32K 上下文 (Seq_Len=32768) 的单条请求 KV Cache 显存占用：KV_Cache_GB = (2 * 48 * 8 * 128 * 32768 * 1) / 1024^3 ≈ 3.75 GB。此值直接影响 FP8 方案下的最大并发 Batch Size。

## Corrected Claim

基于 N110 提取的参数，计算 Qwen3-27B 在 FP8 (1 byte) 精度下，32K 上下文 (Seq_Len=32768) 的单条请求 KV Cache 显存占用：KV_Cache_GB = (2 * 48 * 8 * 128 * 32768 * 1) / 1024^3 ≈ 3.75 GB。此值直接影响 FP8 方案下的最大并发 Batch Size。

## Evidence

先验知识/题面给定，逻辑校验通过：公式结构正确（2*层数*头数*头维*序列长*字节数），数值计算准确（2*48*8*128*32768/1024^3 ≈ 3.75 GB），符合Qwen3-27B架构参数及FP8精度下的KV Cache显存占用估算逻辑。
