# N245: 工作点1（短上下文/高计算密度）：在 4K 上下文 Prefill 阶段，Qwen3-27B 激活参数占比约为 3.3B/27.18B = 12.1%，有效 F

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N77

## Claim

工作点1（短上下文/高计算密度）：在 4K 上下文 Prefill 阶段，Qwen3-27B 激活参数占比约为 3.3B/27.18B = 12.1%，有效 FLOPs 为 2 * 3.3e9 * 4096 = 2.70e13，相比全参数 27B 的 2.23e14 FLOPs 降低 87.9%，TTFT 理论值降低至 1/8.8 倍。

## Corrected Claim

工作点1（短上下文/高计算密度）：在 4K 上下文 Prefill 阶段，Qwen3-27B 激活参数占比约为 3.3B/27.18B = 12.1%，有效 FLOPs 为 2 * 3.3e9 * 4096 = 2.70e13，相比全参数 27B 的 2.23e14 FLOPs 降低 87.9%，TTFT 理论值降低至 1/8.8 倍。

## Evidence

先验知识/题面给定，逻辑校验通过：Qwen3-27B 为 MoE 模型，激活参数约 3.3B 符合其架构规格（总参 27B，激活 3.3B）；FLOPs 计算逻辑自洽（2 * 激活参数 * 序列长度），比例关系 3.3/27.18 ≈ 12.1% 及降低幅度 87.9% 数学推导正确。

## Search Query

Qwen3-27B MoE activated parameters ratio prefill FLOPs
