# N214: RTX 6000 Ada (48GB) 在 BF16 下运行 Qwen3-27B 的总显存需求：权重 54GB > 48GB，故 BF16 单卡不可行；必须使用

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N58

## Claim

RTX 6000 Ada (48GB) 在 BF16 下运行 Qwen3-27B 的总显存需求：权重 54GB > 48GB，故 BF16 单卡不可行；必须使用 INT8 (权重 27GB + KV 4GB + 开销 3GB = 34GB < 48GB) 或 FP8 才能满足 32K 上下文要求，这与 A100 40GB 不同（A100 40GB 连 INT8 都紧张）。

## Corrected Claim

RTX 6000 Ada (48GB) 在 BF16 下运行 Qwen3-27B 的总显存需求：权重 54GB > 48GB，故 BF16 单卡不可行；必须使用 INT8 (权重 27GB + KV 4GB + 开销 3GB = 34GB < 48GB) 或 FP8 才能满足 32K 上下文要求，这与 A100 40GB 不同（A100 40GB 连 INT8 都紧张）。

## Evidence

先验知识/题面给定，逻辑校验通过：Qwen3-27B参数量约27B，BF16权重约54GB，超过RTX 6000 Ada 48GB显存；INT8权重约27GB，加上KV Cache和开销后约34GB，在48GB范围内，逻辑自洽且数值量级合理。
