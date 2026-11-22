# N170: Batch=1 时的总显存需求计算：权重 27GB + KV Cache 8GB (FP16) + 框架开销 4GB = 39GB，超出单卡 RTX 4090 

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N49, N50, N51

## Claim

Batch=1 时的总显存需求计算：权重 27GB + KV Cache 8GB (FP16) + 框架开销 4GB = 39GB，超出单卡 RTX 4090 (24GB)，但低于 2x RTX 4090 (48GB) 容量，确认双卡方案在 Batch=1 下可行且无需 Offload。

## Corrected Claim

Batch=1 时的总显存需求计算：权重 27GB + KV Cache 8GB (FP16) + 框架开销 4GB = 39GB，超出单卡 RTX 4090 (24GB)，但低于 2x RTX 4090 (48GB) 容量，确认双卡方案在 Batch=1 下可行且无需 Offload。

## Evidence

先验知识/题面给定，逻辑校验通过：27+8+4=39GB，且 24GB < 39GB < 48GB，数值量级与硬件规格符合常识，逻辑自洽。
