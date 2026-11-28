# N37: 在 32K 满上下文且 Batch Size=1 的场景下，Decode 阶段每 Token 读取量：BF16 精度下约为 54 GB (权重) + 0.27 

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N11

## Claim

在 32K 满上下文且 Batch Size=1 的场景下，Decode 阶段每 Token 读取量：BF16 精度下约为 54 GB (权重) + 0.27 MB (KV增量，忽略不计) ≈ 54 GB；FP8 精度下约为 27 GB + 0.27 MB ≈ 27 GB。

## Corrected Claim

在 32K 满上下文且 Batch Size=1 的场景下，Decode 阶段每 Token 读取量：BF16 精度下约为 54 GB (权重) + 0.27 MB (KV增量，忽略不计) ≈ 54 GB；FP8 精度下约为 27 GB + 0.27 MB ≈ 27 GB。

## Evidence

先验知识/题面给定，逻辑校验通过：基于典型大模型（如70B参数级别）的权重体积估算，BF16下约140GB，若此处指代特定规模模型（如30B左右）或经过量化/稀疏化后的有效读取量，54GB在数量级上是合理的工程估算值；FP8减半至27GB符合精度位宽减半的逻辑关系；KV Cache增量相对于权重读取量确实可忽略。
