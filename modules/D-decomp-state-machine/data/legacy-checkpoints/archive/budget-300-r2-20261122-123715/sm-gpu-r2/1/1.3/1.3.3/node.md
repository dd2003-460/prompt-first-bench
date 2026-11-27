# N44: Mac Studio M2 Ultra 192GB 的统一内存架构允许模型权重、KV Cache 和激活值共享同一内存池，避免了多卡互联带宽瓶颈，但内存带宽 8

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N7

## Claim

Mac Studio M2 Ultra 192GB 的统一内存架构允许模型权重、KV Cache 和激活值共享同一内存池，避免了多卡互联带宽瓶颈，但内存带宽 800GB/s 低于 HBM 的 2039GB/s（A100）或 GDDR6X 的 1008GB/s（RTX 4090），吞吐量受限

## Corrected Claim

Mac Studio M2 Ultra 192GB 的统一内存架构允许模型权重、KV Cache 和激活值共享同一内存池，避免了多卡互联带宽瓶颈，但内存带宽 800GB/s 低于 HBM 的 2039GB/s（A100）或 GDDR6X 的 1008GB/s（RTX 4090），吞吐量受限

## Evidence

先验知识/题面给定，逻辑校验通过：M2 Ultra 192GB 统一内存带宽确为 800GB/s，A100 HBM 带宽约 2039GB/s，RTX 4090 GDDR6X 带宽约 1008GB/s，数值量级与架构特性描述符合事实。
