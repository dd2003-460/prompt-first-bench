# N34: BF16 精度下，Qwen3-27B 单请求推理的最小显存需求 = 权重 (54 GB) + KV Cache (8.59 GB) + 激活值/中间层缓冲 (估

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N10

## Claim

BF16 精度下，Qwen3-27B 单请求推理的最小显存需求 = 权重 (54 GB) + KV Cache (8.59 GB) + 激活值/中间层缓冲 (估算 2-4 GB) ≈ 64.6 - 66.6 GB。

## Corrected Claim

BF16 精度下，Qwen3-27B 单请求推理的最小显存需求 = 权重 (54 GB) + KV Cache (8.59 GB) + 激活值/中间层缓冲 (估算 2-4 GB) ≈ 64.6 - 66.6 GB。

## Evidence

先验知识/题面给定，逻辑校验通过：Qwen3-27B参数量约27B，BF16权重约54GB；KV Cache及激活值估算符合大模型推理显存占用常规量级，总显存需求64.6-66.6GB在逻辑上自洽且数值合理。
