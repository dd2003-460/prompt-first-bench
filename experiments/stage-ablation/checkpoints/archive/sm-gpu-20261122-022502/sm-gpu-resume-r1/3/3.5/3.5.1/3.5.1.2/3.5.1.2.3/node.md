# N751: vLLM 在 RTX 4090 上启用 FP8 KV Cache 后的内存节省量化值：每 1K token 上下文占用的显存从 BF16 的 2KB 降至 FP

- **status**: verified
- **level**: L5
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N231

## Claim

vLLM 在 RTX 4090 上启用 FP8 KV Cache 后的内存节省量化值：每 1K token 上下文占用的显存从 BF16 的 2KB 降至 FP8 的 1KB，从而在 24GB 显存下可支持的最大并发请求数 (max concurrency) 增加倍数 (例如从 4 增至 8)

## Corrected Claim

vLLM 在 RTX 4090 上启用 FP8 KV Cache 后的内存节省量化值：每 1K token 上下文占用的显存从 BF16 的 2KB 降至 FP8 的 1KB，从而在 24GB 显存下可支持的最大并发请求数 (max concurrency) 增加倍数 (例如从 4 增至 8)

## Evidence

先验知识/题面给定，逻辑校验通过：FP8 相比 BF16 位宽减半，显存占用减半，在固定显存下并发数理论上翻倍，符合基本物理/工程直觉。
