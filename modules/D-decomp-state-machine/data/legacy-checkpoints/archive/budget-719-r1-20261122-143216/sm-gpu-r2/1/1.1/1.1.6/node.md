# N41: 激活值缓冲（Activation Buffer）在 32K 上下文、batch_size=1 时的显存占用（GB），计算公式涉及 hidden_size × s

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N6, N7, N8

## Claim

激活值缓冲（Activation Buffer）在 32K 上下文、batch_size=1 时的显存占用（GB），计算公式涉及 hidden_size × seq_len × bytes_per_elem × 层数因子，需基于具体模型参数计算。

## Corrected Claim

激活值缓冲（Activation Buffer）在 32K 上下文、batch_size=1 时的显存占用（GB），计算公式涉及 hidden_size × seq_len × bytes_per_elem × 层数因子，需基于具体模型参数计算。

## Evidence

先验知识/题面给定，逻辑校验通过：激活值显存占用确实依赖于 hidden_size、seq_len、数据类型字节数及层数（或特定优化策略下的因子），公式结构符合深度学习推理显存估算的基本原理。
