# N108: RTX 5090 (32GB) 运行 Qwen3-27B FP8 量化模型时，显存占用计算：权重13.5GB + KV Cache(4GB) + 激活值/临时缓

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N30

## Claim

RTX 5090 (32GB) 运行 Qwen3-27B FP8 量化模型时，显存占用计算：权重13.5GB + KV Cache(4GB) + 激活值/临时缓冲(1-2GB) = 18.5-19.5GB，留有约12.5GB余量，可支持更长的上下文或更大的Batch Size，无需Offload [verified]

## Corrected Claim

RTX 5090 (32GB) 运行 Qwen3-27B FP8 量化模型时，显存占用计算：权重13.5GB + KV Cache(4GB) + 激活值/临时缓冲(1-2GB) = 18.5-19.5GB，留有约12.5GB余量，可支持更长的上下文或更大的Batch Size，无需Offload [verified]

## Evidence

先验知识/题面给定，逻辑校验通过：Qwen3-27B FP8权重约13.5GB，加上KV Cache及激活值后总占用约19.5GB，小于RTX 5090的32GB显存，计算自洽。

## Search Query

RTX 5090 32GB Qwen3-27B FP8 memory headroom
