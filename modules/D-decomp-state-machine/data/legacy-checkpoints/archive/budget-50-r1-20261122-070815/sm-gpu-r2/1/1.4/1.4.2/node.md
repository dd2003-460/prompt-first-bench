# N44: Qwen3-27B 在 FP8 精度下的权重显存占用为 27 GB，加上 32K 上下文 KV Cache (约 1.07 GB) 及 15% 开销，总需求约 

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N9

## Claim

Qwen3-27B 在 FP8 精度下的权重显存占用为 27 GB，加上 32K 上下文 KV Cache (约 1.07 GB) 及 15% 开销，总需求约 32.4 GB，超过 RTX 4090 的 24 GB 单卡显存上限，单卡 FP8 方案不可行

## Corrected Claim

Qwen3-27B 在 FP8 精度下的权重显存占用为 27 GB，加上 32K 上下文 KV Cache (约 1.07 GB) 及 15% 开销，总需求约 32.4 GB，超过 RTX 4090 的 24 GB 单卡显存上限，单卡 FP8 方案不可行

## Evidence

先验知识/题面给定，逻辑校验通过：27B参数在FP8下权重约27GB，加上KV Cache及开销后总显存需求约32.4GB，确实超过RTX 4090的24GB显存上限，单卡不可行。
