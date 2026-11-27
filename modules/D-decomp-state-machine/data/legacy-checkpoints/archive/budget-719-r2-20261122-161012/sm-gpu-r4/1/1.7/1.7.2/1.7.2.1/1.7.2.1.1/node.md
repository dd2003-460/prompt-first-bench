# N439: Qwen3-27B 每 token 的 KV Cache 增量（BF16）：KV_per_token = 2 * 64 * 8 * 128 * 2 = 262,

- **status**: verified
- **level**: L5
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N183

## Claim

Qwen3-27B 每 token 的 KV Cache 增量（BF16）：KV_per_token = 2 * 64 * 8 * 128 * 2 = 262,144 bytes = 256 KiB。这意味着每增加 1 个 token 上下文，显存占用增加 256 KiB。

## Corrected Claim

Qwen3-27B 每 token 的 KV Cache 增量（BF16）：KV_per_token = 2 * 64 * 8 * 128 * 2 = 262,144 bytes = 256 KiB。这意味着每增加 1 个 token 上下文，显存占用增加 256 KiB。

## Evidence

先验知识/题面给定，逻辑校验通过：Qwen3-27B 架构参数（GQA, 8 KV heads, 128 head_dim, 64 layers）符合公开技术报告，BF16 下每 token KV Cache 计算 2*64*8*128*2=262,144 bytes 正确。

## Search Query

Qwen3-27B kv cache per token bytes
