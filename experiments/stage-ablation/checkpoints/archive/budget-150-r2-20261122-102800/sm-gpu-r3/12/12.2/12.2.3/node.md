# N413: 长序列 (32K) 下 KV Cache 占用为 4.29 GB (BF16)，RTX 4090 (24GB) 可容纳权重 (13.5GB W4) + KV (

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N164

## Claim

长序列 (32K) 下 KV Cache 占用为 4.29 GB (BF16)，RTX 4090 (24GB) 可容纳权重 (13.5GB W4) + KV (4.29GB) ≈ 17.8GB，无 Offload 需求。A100 40GB 和 H100 80GB 同样无 Offload 需求。此时硬件差异主要在于内存带宽，而非显存容量。

## Corrected Claim

长序列 (32K) 下 KV Cache 占用为 4.29 GB (BF16)，RTX 4090 (24GB) 可容纳权重 (13.5GB W4) + KV (4.29GB) ≈ 17.8GB，无 Offload 需求。A100 40GB 和 H100 80GB 同样无 Offload 需求。此时硬件差异主要在于内存带宽，而非显存容量。

## Evidence

先验知识/题面给定，逻辑校验通过：KV Cache 占用量级符合 32K 序列 BF16 的典型估算（约 4-5GB），RTX 4090 24GB 显存容纳 13.5GB 权重 + 4.29GB KV 后剩余空间充足，无需 Offload 的结论在逻辑和工程常识上均成立。
