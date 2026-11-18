# N148: FP8 KV Cache 在代码生成任务 (HumanEval Pass@1) 上的质量损失通常小于 1-2% (例如从 90% 降至 88-89%)，远低于 

- **status**: degraded
- **level**: L4
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N43

## Claim

FP8 KV Cache 在代码生成任务 (HumanEval Pass@1) 上的质量损失通常小于 1-2% (例如从 90% 降至 88-89%)，远低于 W4 权重量化的损失 (通常 >5%)，因为 KV Cache 主要影响注意力机制的精度，对生成逻辑的结构性影响较小，但需通过具体任务基准验证。

## Corrected Claim

FP8 KV Cache 量化通常能显著降低内存占用且对生成质量影响较小（通常优于 W4 权重量化），但具体在 HumanEval 等基准上的质量损失需根据具体模型和实现进行验证。

## Evidence

[质询]具体数值（HumanEval Pass@1 损失 <1-2% 及 W4 损失 >5%）属于经验事实，参考来源未提供该特定基准测试的直接数据支持，且不同模型和量化实现下数值可能存在波动。 | 来源 [3] 证实 FP8 用于 KV Cache 是 LLM 推理/RL 中的常见优化手段，支持了技术可行性，但未提供 HumanEval 具体质量损失数值；逻辑上 KV Cache 量化对生成逻辑影响小于权重量化符合直觉，但具体数值缺乏直接来源支持，故降级。

## Search Query

FP8 KV cache impact on code generation accuracy HumanEval Pass@1

## Retrieval Sources

- {'url': 'https://arxiv.org', 'type': None, 'title': 'direct-browser: arxiv.org'}
- {'url': 'https://github.com', 'type': None, 'title': 'direct-browser: github.com'}
- {'url': 'http://arxiv.org/abs/2601.18150v2', 'type': 'arxiv', 'title': 'FP8-RL: A Practical and Stable Low-Precision Stack for LLM Reinforcement Learnin'}
