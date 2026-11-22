# N37: Batch Size 对额外开销的非线性影响：当 Batch Size > 1 时，KV Cache 和激活值显存随 Batch Size 线性增长。需计算在目

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N8

## Claim

Batch Size 对额外开销的非线性影响：当 Batch Size > 1 时，KV Cache 和激活值显存随 Batch Size 线性增长。需计算在目标并发数（如 Batch=4 或 8）下，总显存需求是否超出单卡/双卡容量，这直接影响硬件选型（单卡 vs 多卡）。

## Corrected Claim

Batch Size 对额外开销的非线性影响：当 Batch Size > 1 时，KV Cache 和激活值显存随 Batch Size 线性增长。需计算在目标并发数（如 Batch=4 或 8）下，总显存需求是否超出单卡/双卡容量，这直接影响硬件选型（单卡 vs 多卡）。

## Evidence

先验知识/题面给定，逻辑校验通过：KV Cache 和激活值显存确实随 Batch Size 线性增长，这是大模型推理显存估算的基本原理。
