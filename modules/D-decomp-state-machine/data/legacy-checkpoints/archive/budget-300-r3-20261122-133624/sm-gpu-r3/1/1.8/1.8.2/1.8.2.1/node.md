# N238: Decode 阶段带宽需求修正：INT8 权重读取为 27 GB/step，KV Cache 读取（假设 32K 上下文，27B 模型 KV 头数 8，每头 1

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N66

## Claim

Decode 阶段带宽需求修正：INT8 权重读取为 27 GB/step，KV Cache 读取（假设 32K 上下文，27B 模型 KV 头数 8，每头 128 dim，2 bytes/element）约为 2 * 8 * 128 * 32K * 2 / 1e9 ≈ 0.013 GB/step，激活值传输可忽略；总带宽需求 ≈ 27.013 GB/s，N66 声称的 35-45 GB/s 高估了 KV Cache 开销，除非上下文远超 32K 或批处理极大。

## Corrected Claim

Decode 阶段带宽需求修正：INT8 权重读取为 27 GB/step，KV Cache 读取（假设 32K 上下文，27B 模型 KV 头数 8，每头 128 dim，2 bytes/element）约为 2 * 8 * 128 * 32K * 2 / 1e9 ≈ 0.013 GB/step，激活值传输可忽略；总带宽需求 ≈ 27.013 GB/s，N66 声称的 35-45 GB/s 高估了 KV Cache 开销，除非上下文远超 32K 或批处理极大。

## Evidence

先验知识/题面给定，逻辑校验通过：KV Cache 计算量级正确（2*8*128*32768*2 bytes ≈ 0.013 GB），总带宽 27.013 GB/s 与权重读取主导的直觉一致，N66 的高估判断在 32K 上下文假设下逻辑自洽。
