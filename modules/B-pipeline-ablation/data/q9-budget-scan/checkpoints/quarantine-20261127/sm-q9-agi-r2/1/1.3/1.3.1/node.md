# N37: MTP×4 (Multi-Token Prediction) 在 Qwen3.8-27B 上的接受率 α 并非恒定 0.6-0.8，而是随任务复杂度动态变化：在

- **status**: degraded
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N9

## Claim

MTP×4 (Multi-Token Prediction) 在 Qwen3.8-27B 上的接受率 α 并非恒定 0.6-0.8，而是随任务复杂度动态变化：在代码生成/数学推理等高熵任务中，α 通常降至 0.4-0.5；在文本续写/低熵任务中，α 可达 0.8-0.9。科研循环中的‘假设生成’属于高创造性任务，预期 α ≈ 0.5。

## Corrected Claim

MTP×4 在 Qwen3.8-27B 上的接受率 α 随任务复杂度动态变化：在高熵任务（如代码生成/数学推理）中通常低于低熵任务（如文本续写），科研假设生成等高创造性任务的预期接受率相对较低。

## Evidence

[质询]具体数值区间（如代码任务0.4-0.5，低熵任务0.8-0.9）及特定模型（Qwen3.8-27B）的MTP接受率缺乏公开基准数据支持，属于未经证实的经验性断言，可能存在过度精确化或虚构具体参数的风险。 | 先验知识/题面给定，逻辑校验通过（高熵任务接受率低符合直觉），但具体数值缺乏来源支持，故降级。

## Search Query

speculative decoding acceptance rate variance by task type high entropy
