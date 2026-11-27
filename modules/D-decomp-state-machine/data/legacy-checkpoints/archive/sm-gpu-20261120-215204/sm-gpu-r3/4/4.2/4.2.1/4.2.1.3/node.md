# N280: FP8 量化对任务敏感度的放大机制：数学/代码任务依赖逻辑链条的长程依赖，量化误差在 Transformer 层间累积（Error Accumulation），

- **status**: degraded
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N98, N99, N100

## Claim

FP8 量化对任务敏感度的放大机制：数学/代码任务依赖逻辑链条的长程依赖，量化误差在 Transformer 层间累积（Error Accumulation），导致最终 Token 概率分布偏移比通用文本生成（WikiText）更显著，量化误差传播系数约为通用任务的 2-3 倍

## Corrected Claim

FP8 量化对任务敏感度的放大机制：数学/代码任务依赖逻辑链条的长程依赖，量化误差在 Transformer 层间累积（Error Accumulation），导致最终 Token 概率分布偏移比通用文本生成（WikiText）更显著，量化误差传播效应通常显著高于通用任务。

## Evidence

[质询]「量化误差传播系数约为通用任务的 2-3 倍」这一具体数值缺乏普遍公认的基准，不同模型架构、量化方案（如 SmoothQuant, GPTQ）及任务定义下，误差放大倍数波动极大，该具体倍数可能源自特定实验而非普适规律，存在以偏概全的风险。 | 先验知识/题面给定，逻辑校验通过：数学/代码任务确实对长程依赖和精确逻辑更敏感，量化误差累积导致性能下降通常高于通用文本生成，但具体倍数属于经验性观察，缺乏统一标准，故降级为定性表述。
