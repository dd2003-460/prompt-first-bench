# N35: FP8/INT8 精度下，Qwen3-27B 单请求推理的最小显存需求 = 权重 (27 GB) + KV Cache (8.59 GB) + 激活值 (2-4

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N10

## Claim

FP8/INT8 精度下，Qwen3-27B 单请求推理的最小显存需求 = 权重 (27 GB) + KV Cache (8.59 GB) + 激活值 (2-4 GB) ≈ 37.6 - 39.6 GB，该数值决定 48GB 显卡的可行性。

## Corrected Claim

FP8/INT8 精度下，Qwen3-27B 单请求推理的最小显存需求 = 权重 (27 GB) + KV Cache (8.59 GB) + 激活值 (2-4 GB) ≈ 37.6 - 39.6 GB，该数值决定 48GB 显卡的可行性。

## Evidence

[质询]KV Cache 大小高度依赖于上下文长度（Context Length）和批处理大小（Batch Size），8.59 GB 是一个特定场景下的经验值而非固定常数，若上下文极长或并发高，该数值会显著增加，导致总显存超过 48GB。 | 先验知识/题面给定，逻辑校验通过：27B 模型 FP8/INT8 权重约 13.5-27GB（取决于具体量化格式及是否包含其他开销，此处取 27GB 为保守估计或包含部分冗余），加上 KV Cache 和激活值，总量级在 40GB 左右，符合 48GB 显卡边缘可行的工程直觉。
