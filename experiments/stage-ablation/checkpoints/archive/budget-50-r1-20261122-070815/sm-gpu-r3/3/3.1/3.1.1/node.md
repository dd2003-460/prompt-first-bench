# N74: 在 Decode 阶段，单 token 生成速度 (tokens/s) 的理论上限近似等于 显存带宽(GB/s) / 每次生成需读取的总字节数，其中总字节数 =

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N18

## Claim

在 Decode 阶段，单 token 生成速度 (tokens/s) 的理论上限近似等于 显存带宽(GB/s) / 每次生成需读取的总字节数，其中总字节数 = 模型权重大小(GB) + KV Cache 每 token 增量(GB)

## Corrected Claim

在 Decode 阶段，单 token 生成速度 (tokens/s) 的理论上限近似等于 显存带宽(GB/s) / 每次生成需读取的总字节数，其中总字节数 = 模型权重大小(GB) + KV Cache 每 token 增量(GB)

## Evidence

先验知识/题面给定，逻辑校验通过
