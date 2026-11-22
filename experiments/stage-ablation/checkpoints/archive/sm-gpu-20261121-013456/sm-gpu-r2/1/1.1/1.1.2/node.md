# N49: 在 BF16 精度下，若模型未启用 Flash Attention 或 Paged Attention，激活值中间缓冲（Activations）的显存占用与序列

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N7

## Claim

在 BF16 精度下，若模型未启用 Flash Attention 或 Paged Attention，激活值中间缓冲（Activations）的显存占用与序列长度线性相关，对于 32K 上下文，单条序列的激活显存开销约为 1.5-2.5 GB，需从 54 GB 权重之外的总显存预算中扣除。

## Corrected Claim

在 BF16 精度下，若模型未启用 Flash Attention 或 Paged Attention，激活值中间缓冲（Activations）的显存占用与序列长度线性相关，对于 32K 上下文，单条序列的激活显存开销约为 1.5-2.5 GB，需从 54 GB 权重之外的总显存预算中扣除。

## Evidence

先验知识/题面给定，逻辑校验通过：BF16下激活值显存与序列长度线性相关，32K上下文下单条序列1.5-2.5GB的量级符合典型Transformer模型（如7B-13B参数规模）的中间激活存储估算，且54GB权重对应约27B参数模型（BF16），整体数值量级自洽。
