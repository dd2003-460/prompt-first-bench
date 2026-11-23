# N6: Qwen3-27B 在 BF16 下的权重内存占用为 54GB，加上 32K 上下文 KV Cache（假设 GQA 8:1，hidden 4096，32 层，

- **status**: verified
- **level**: L2
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N1, N2, N3

## Claim

Qwen3-27B 在 BF16 下的权重内存占用为 54GB，加上 32K 上下文 KV Cache（假设 GQA 8:1，hidden 4096，32 层，每 token 约 0.25MB）约 8GB，总需求约 62GB；若使用 FP8 量化，权重降至 27GB，总需求约 35GB。

## Corrected Claim

Qwen3-27B 在 BF16 下的权重内存占用为 54GB，加上 32K 上下文 KV Cache（假设 GQA 8:1，hidden 4096，32 层，每 token 约 0.25MB）约 8GB，总需求约 62GB；若使用 FP8 量化，权重降至 27GB，总需求约 35GB。

## Evidence

先验知识/题面给定，逻辑校验通过：27B参数BF16权重约54GB，FP8约27GB；KV Cache计算（32K tokens * 0.25MB/token = 8GB）符合给定假设下的算术逻辑，总内存估算自洽。
