# N229: W4权重+INT8 KV Cache配置下，总显存需求为23.27GB（权重13.92GB+KV 5.35GB+框架4GB）。此配置下单卡RTX 4090 (2

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N77

## Claim

W4权重+INT8 KV Cache配置下，总显存需求为23.27GB（权重13.92GB+KV 5.35GB+框架4GB）。此配置下单卡RTX 4090 (24GB)理论上可行，但剩余显存仅约0.73GB，不足以支持32K上下文的KV Cache动态分配，实际仍需Offload或降低上下文长度至16K以下。

## Corrected Claim

W4权重+INT8 KV Cache配置下，总显存需求为23.27GB（权重13.92GB+KV 5.35GB+框架4GB）。此配置下单卡RTX 4090 (24GB)理论上可行，但剩余显存仅约0.73GB，不足以支持32K上下文的KV Cache动态分配，实际仍需Offload或降低上下文长度至16K以下。

## Evidence

先验知识/题面给定，逻辑校验通过：23.27GB < 24GB 且剩余 0.73GB 确实不足以支撑 32K 上下文动态 KV Cache 增长，符合显存管理基本逻辑。
