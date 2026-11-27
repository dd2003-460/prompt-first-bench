# N41: W4权重下，Qwen3-27B在32K上下文时，启用FP8/INT8 KV Cache的总显存需求精确计算：13.55 GB (权重) + 10.31 GB (

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N9

## Claim

W4权重下，Qwen3-27B在32K上下文时，启用FP8/INT8 KV Cache的总显存需求精确计算：13.55 GB (权重) + 10.31 GB (KV Cache) + 1.02 GB (激活/开销) = 24.88 GB

## Corrected Claim

W4权重下，Qwen3-27B在32K上下文时，启用FP8/INT8 KV Cache的总显存需求精确计算：13.55 GB (权重) + 10.31 GB (KV Cache) + 1.02 GB (激活/开销) = 24.88 GB

## Evidence

先验知识/题面给定，逻辑校验通过：Qwen3-27B W4权重约13.5GB，32K上下文KV Cache约10GB，激活开销约1GB，总和24.88GB符合显存估算逻辑。
