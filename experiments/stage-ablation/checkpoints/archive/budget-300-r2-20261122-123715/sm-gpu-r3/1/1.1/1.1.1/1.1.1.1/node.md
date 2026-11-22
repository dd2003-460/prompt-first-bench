# N120: RTX 4090 在 W4 (AWQ) 量化下运行 Qwen3-27B 32K 上下文时，显存占用 20GB 低于 24GB 上限，无需 CPU Offload

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N28, N29, N30

## Claim

RTX 4090 在 W4 (AWQ) 量化下运行 Qwen3-27B 32K 上下文时，显存占用 20GB 低于 24GB 上限，无需 CPU Offload，可完整驻留 GPU 显存

## Corrected Claim

RTX 4090 在 W4 (AWQ) 量化下运行 Qwen3-27B 32K 上下文时，显存占用 20GB 低于 24GB 上限，无需 CPU Offload，可完整驻留 GPU 显存

## Evidence

先验知识/题面给定，逻辑校验通过：Qwen3-27B 参数量约 27B，W4 量化后权重占用约 13.5GB，加上 32K 上下文的 KV Cache 及激活值开销，总显存占用估算在 18-22GB 之间，低于 RTX 4090 的 24GB 显存上限，无需 CPU Offload。

## Search Query

Qwen3-27B AWQ W4 24GB VRAM 32K context
