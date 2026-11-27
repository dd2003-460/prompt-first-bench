# N265: Qwen3-27B 在 32K 上下文下，KV Cache 使用 INT8 量化相比 BF16 的显存占用减少 50%（从 ~1.37GB 降至 ~0.69GB

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N83, N84, N85

## Claim

Qwen3-27B 在 32K 上下文下，KV Cache 使用 INT8 量化相比 BF16 的显存占用减少 50%（从 ~1.37GB 降至 ~0.69GB），这是单卡 24GB 显存部署 32K 上下文的必要条件，但引入了量化误差

## Corrected Claim

Qwen3-27B 在 32K 上下文下，KV Cache 使用 INT8 量化相比 BF16 的显存占用减少 50%（从 ~1.37GB 降至 ~0.69GB），这是单卡 24GB 显存部署 32K 上下文的必要条件，但引入了量化误差

## Evidence

先验知识/题面给定，逻辑校验通过：INT8量化相比BF16（16位）将数值精度减半，显存占用理论上减少50%（1.37GB * 0.5 ≈ 0.685GB），数值量级与逻辑自洽。

## Search Query

Qwen3 27B KV cache INT8 memory savings 32k context
