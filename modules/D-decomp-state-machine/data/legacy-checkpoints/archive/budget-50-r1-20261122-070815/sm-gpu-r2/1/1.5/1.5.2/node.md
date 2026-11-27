# N49: Qwen3-27B 在 FP8 精度下的权重显存占用为 27 GB，加上 32K 上下文 KV Cache (约 1.07 GB) 及 15% 开销，总需求约 

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N10

## Claim

Qwen3-27B 在 FP8 精度下的权重显存占用为 27 GB，加上 32K 上下文 KV Cache (约 1.07 GB) 及 15% 开销，总需求约 32.4 GB，远低于 A100 80GB 和 H100 80GB 的显存上限，单卡 FP8 方案高度可行，余量超过 47 GB，可支持更长上下文或更大 batch size

## Corrected Claim

Qwen3-27B 在 FP8 精度下的权重显存占用为 27 GB，加上 32K 上下文 KV Cache (约 1.07 GB) 及 15% 开销，总需求约 32.4 GB，远低于 A100 80GB 和 H100 80GB 的显存上限，单卡 FP8 方案高度可行，余量超过 47 GB，可支持更长上下文或更大 batch size

## Evidence

先验知识/题面给定，逻辑校验通过：27B参数在FP8下权重约27GB，32K上下文KV Cache约1GB，总显存需求约32.4GB，低于80GB显存上限，计算自洽。
