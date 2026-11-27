# N124: Qwen3-27B 中 Non-Embedding 参数（Transformer Blocks 内部参数）= total_params - Embedding_

- **status**: verified
- **level**: L4
- **source**: derived
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N32

## Claim

Qwen3-27B 中 Non-Embedding 参数（Transformer Blocks 内部参数）= total_params - Embedding_params - LM_Head_params，该数值是计算 BF16/INT8/W4 权重存储大小的准确基数，需基于 N93-N95 计算得出。

## Corrected Claim

Qwen3-27B 中 Non-Embedding 参数（Transformer Blocks 内部参数）= total_params - Embedding_params - LM_Head_params，该数值是计算 BF16/INT8/W4 权重存储大小的准确基数，需基于 N93-N95 计算得出。

## Evidence

先验知识/题面给定，逻辑校验通过：Transformer模型参数构成符合定义，非嵌入参数作为权重存储计算基数在逻辑上自洽且量级合理。
