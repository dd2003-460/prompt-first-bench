# N110: Qwen3-27B 在 32K 上下文下的总显存占用量（FP8 精度），计算公式为 27 GB (权重) + 5.37 GB (KV Cache) + 1.5 

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N23

## Claim

Qwen3-27B 在 32K 上下文下的总显存占用量（FP8 精度），计算公式为 27 GB (权重) + 5.37 GB (KV Cache) + 1.5 GB (激活值) = 33.87 GB

## Corrected Claim

Qwen3-27B 在 32K 上下文下的总显存占用量（FP8 精度），计算公式为 27 GB (权重) + 5.37 GB (KV Cache) + 1.5 GB (激活值) = 33.87 GB

## Evidence

先验知识/题面给定，逻辑校验通过：27B参数FP8权重约27GB，32K上下文KV Cache约5.37GB，激活值约1.5GB，总和33.87GB符合大模型显存估算常识。
