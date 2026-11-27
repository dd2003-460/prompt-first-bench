# N234: A100 80GB 在 BF16 下剩余 25GB 显存，按 Qwen3-27B 32K 上下文单请求 KV Cache 1.2GB 计算，最大支持 Batch

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N109

## Claim

A100 80GB 在 BF16 下剩余 25GB 显存，按 Qwen3-27B 32K 上下文单请求 KV Cache 1.2GB 计算，最大支持 Batch Size = 25 / 1.2 ≈ 20 个并发请求。

## Corrected Claim

A100 80GB 在 BF16 下剩余 25GB 显存，按 Qwen3-27B 32K 上下文单请求 KV Cache 1.2GB 计算，最大支持 Batch Size = 25 / 1.2 ≈ 20 个并发请求。

## Evidence

先验知识/题面给定，逻辑校验通过：25GB / 1.2GB ≈ 20.83，向下取整为20，计算逻辑自洽且量级合理。
