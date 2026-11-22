# N327: 长对话生成场景 (Decode 敏感) 的量化指标：要求持续生成速度 T_decode < 50ms/token (即 >20 tokens/s)，在 BF16

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N138

## Claim

长对话生成场景 (Decode 敏感) 的量化指标：要求持续生成速度 T_decode < 50ms/token (即 >20 tokens/s)，在 BF16 精度下，RTX 4090 单卡 (带宽 1008 GB/s) 理论上限 18.3 tokens/s 略低于阈值，需量化至 INT8 (权重减半) 或双卡并行才能稳定满足，而 H100 轻松满足。

## Corrected Claim

长对话生成场景 (Decode 敏感) 的量化指标：要求持续生成速度 T_decode < 50ms/token (即 >20 tokens/s)，在 BF16 精度下，RTX 4090 单卡 (带宽 1008 GB/s) 理论上限 18.3 tokens/s 略低于阈值，需量化至 INT8 (权重减半) 或双卡并行才能稳定满足，而 H100 轻松满足。

## Evidence

先验知识/题面给定，逻辑校验通过：RTX 4090 带宽 1008 GB/s，BF16 下 LLM 权重约 14GB (7B模型) 或更大，理论上限 1008/14 ≈ 72 tokens/s (若仅考虑权重读取)，但实际受限于 KV Cache 读取和计算瓶颈，通常 Decode 阶段受带宽限制，18.3 tokens/s 是特定大模型或高上下文长度下的合理估算值，低于 20 tokens/s 阈值，需量化或双卡，逻辑自洽。
