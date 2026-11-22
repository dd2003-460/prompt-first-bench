# N87: NVIDIA L40S 48GB 在 Qwen3-27B FP8 精度下的显存占用为 27GB (权重) + 8.4GB (KV Cache) + 2GB (激

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N22

## Claim

NVIDIA L40S 48GB 在 Qwen3-27B FP8 精度下的显存占用为 27GB (权重) + 8.4GB (KV Cache) + 2GB (激活) = 37.4GB，剩余 10.6GB 显存可用于增加并发或更长上下文，显存利用率约 77.92%。

## Corrected Claim

NVIDIA L40S 48GB 在 Qwen3-27B FP8 精度下的显存占用为 27GB (权重) + 8.4GB (KV Cache) + 2GB (激活) = 37.4GB，剩余 10.6GB 显存可用于增加并发或更长上下文，显存利用率约 77.92%。

## Evidence

先验知识/题面给定，逻辑校验通过：Qwen3-27B FP8权重约27GB，KV Cache与激活值估算合理，总占用37.4GB小于48GB，利用率计算正确。
