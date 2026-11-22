# N55: 每步权重加载体积量化：Model_Weight_GB = Params × Bytes_per_param × (1/Seq_Len_factor)，对于自回归

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N11

## Claim

每步权重加载体积量化：Model_Weight_GB = Params × Bytes_per_param × (1/Seq_Len_factor)，对于自回归生成，每步需加载全部权重（假设无 KV 复用优化），即 27B × 2 (BF16) = 54 GB；若使用 KV Cache 优化，实际加载量可能降低，但保守估计取全量。

## Corrected Claim

每步权重加载体积量化：Model_Weight_GB = Params × Bytes_per_param × (1/Seq_Len_factor)，对于自回归生成，每步需加载全部权重（假设无 KV 复用优化），即 27B × 2 (BF16) = 54 GB；若使用 KV Cache 优化，实际加载量可能降低，但保守估计取全量。

## Evidence

先验知识/题面给定，逻辑校验通过：27B参数在BF16下每参数2字节，总权重54GB，自回归生成每步需加载全部权重（无KV复用优化时），量纲与数值量级合理。
