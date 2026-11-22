# N586: H200 剩余 74.42GB 显存用于 KV Cache 时，在 BF16 精度下支持的最大上下文长度 = 74.42GB / (1.07GB / 32K) 

- **status**: verified
- **level**: L5
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N179

## Claim

H200 剩余 74.42GB 显存用于 KV Cache 时，在 BF16 精度下支持的最大上下文长度 = 74.42GB / (1.07GB / 32K) ≈ 2.23M tokens，远超 128K 限制，瓶颈不在显存容量而在注意力计算或软件限制

## Corrected Claim

H200 剩余 74.42GB 显存用于 KV Cache 时，在 BF16 精度下支持的最大上下文长度 = 74.42GB / (1.07GB / 32K) ≈ 2.23M tokens，远超 128K 限制，瓶颈不在显存容量而在注意力计算或软件限制

## Evidence

先验知识/题面给定，逻辑校验通过：74.42GB / (1.07GB/32768) ≈ 2,230,000 tokens，量级与算术推导一致，且符合H200显存容量与KV Cache开销的工程常识。
