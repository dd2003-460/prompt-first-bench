# N47: FP8/INT8 精度下 Qwen3-27B 的总显存硬性需求为 45.11 GB（权重 27 GB + KV Cache 13.11 GB + 运行时开销 5

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N10

## Claim

FP8/INT8 精度下 Qwen3-27B 的总显存硬性需求为 45.11 GB（权重 27 GB + KV Cache 13.11 GB + 运行时开销 5 GB），导致单卡 48GB (L40S/A30) 或 2×24GB 消费级显卡成为最小可行配置，单卡 24GB 显卡不可行

## Corrected Claim

FP8/INT8 精度下 Qwen3-27B 的总显存硬性需求为 45.11 GB（权重 27 GB + KV Cache 13.11 GB + 运行时开销 5 GB），导致单卡 48GB (L40S/A30) 或 2×24GB 消费级显卡成为最小可行配置，单卡 24GB 显卡不可行

## Evidence

先验知识/题面给定，逻辑校验通过：27B参数在FP8/INT8下权重约27GB，加上KV Cache和运行时开销，总显存需求约45GB，单卡24GB确实不足，48GB或双卡24GB为合理最小配置。
