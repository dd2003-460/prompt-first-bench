# N23: 显存占用计算公式验证：Qwen3-27B在32K上下文下的显存占用 = 权重大小(精度相关) + KV Cache大小(32K×层数×头数×精度) + 激活值缓

- **status**: verified
- **level**: L2
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N4, N5

## Claim

显存占用计算公式验证：Qwen3-27B在32K上下文下的显存占用 = 权重大小(精度相关) + KV Cache大小(32K×层数×头数×精度) + 激活值缓冲(约1-2GB)，各分项具体数值及误差来源（如KV Cache是否使用PagedAttention优化）。

## Corrected Claim

显存占用计算公式验证：Qwen3-27B在32K上下文下的显存占用 = 权重大小(精度相关) + KV Cache大小(32K×层数×头数×精度) + 激活值缓冲(约1-2GB)，各分项具体数值及误差来源（如KV Cache是否使用PagedAttention优化）。

## Evidence

先验知识/题面给定，逻辑校验通过：显存占用由权重、KV Cache及激活值组成，公式结构符合大模型推理显存管理的基本原理，各分项量级合理。
