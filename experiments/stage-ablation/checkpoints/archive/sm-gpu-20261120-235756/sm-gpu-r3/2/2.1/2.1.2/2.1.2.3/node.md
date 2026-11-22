# N188: 单流推理中激活值显存的预留策略：尽管Batch_Size=1时激活值占2.6 GB (约占总显存需求的3-5%)，但需预留10-15%的安全边际以应对注意力计算

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N57

## Claim

单流推理中激活值显存的预留策略：尽管Batch_Size=1时激活值占2.6 GB (约占总显存需求的3-5%)，但需预留10-15%的安全边际以应对注意力计算中的临时缓冲区（如Softmax中间结果），因此实际预留应为3-4 GB，而非忽略不计。

## Corrected Claim

单流推理中激活值显存的预留策略：尽管Batch_Size=1时激活值占2.6 GB (约占总显存需求的3-5%)，但需预留10-15%的安全边际以应对注意力计算中的临时缓冲区（如Softmax中间结果），因此实际预留应为3-4 GB，而非忽略不计。

## Evidence

先验知识/题面给定，逻辑校验通过

## Search Query

LLM inference activation memory safety margin
