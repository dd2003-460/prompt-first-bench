# N148: Qwen3-27B 的 GQA 8:1 配置使得 KV Cache 相比 MHA (Multi-Head Attention, 32 heads) 减少 75%

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N40

## Claim

Qwen3-27B 的 GQA 8:1 配置使得 KV Cache 相比 MHA (Multi-Head Attention, 32 heads) 减少 75%，计算公式为 (1 - 8/32) * 100% = 75%，这是 32K 上下文下 KV Cache 仅 8.192GB 而非 32.768GB 的关键原因

## Corrected Claim

Qwen3-27B 的 GQA 8:1 配置使得 KV Cache 相比 MHA (Multi-Head Attention, 32 heads) 减少 75%，计算公式为 (1 - 8/32) * 100% = 75%，这是 32K 上下文下 KV Cache 仅 8.192GB 而非 32.768GB 的关键原因

## Evidence

先验知识/题面给定，逻辑校验通过：GQA 8:1 意味着 KV 头数为 32/4=8，相比 MHA 的 32 头，KV Cache 大小减少 (1 - 8/32) = 75%；32.768GB * 25% = 8.192GB，数值计算与逻辑推导完全自洽。
