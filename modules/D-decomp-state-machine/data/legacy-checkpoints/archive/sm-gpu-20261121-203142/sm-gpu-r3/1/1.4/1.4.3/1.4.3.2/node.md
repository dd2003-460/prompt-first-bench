# N164: KV Cache FP8 量化对解码速度 (TPS) 的提升量化：由于 KV Cache 读取量减半 (6GB -> 3GB)，在带宽受限的解码阶段，理论 TP

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N48

## Claim

KV Cache FP8 量化对解码速度 (TPS) 的提升量化：由于 KV Cache 读取量减半 (6GB -> 3GB)，在带宽受限的解码阶段，理论 TPS 提升幅度约为 50% (若仅考虑 KV Cache 读取) 或根据 Roofline 模型重新计算的加速比。

## Corrected Claim

KV Cache FP8 量化对解码速度 (TPS) 的提升量化：由于 KV Cache 读取量减半 (6GB -> 3GB)，在带宽受限的解码阶段，理论 TPS 提升幅度约为 50% (若仅考虑 KV Cache 读取) 或根据 Roofline 模型重新计算的加速比。

## Evidence

先验知识/题面给定，逻辑校验通过：FP8量化使KV Cache体积减半，在带宽受限场景下，读取时间减半理论上可带来约50%的吞吐提升（基于Roofline模型及线性近似），符合基本物理直觉。
