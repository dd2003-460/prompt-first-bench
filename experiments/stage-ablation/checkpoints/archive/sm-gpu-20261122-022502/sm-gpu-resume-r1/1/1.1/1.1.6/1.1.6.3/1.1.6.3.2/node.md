# N480: 量化误差随序列长度累积的机制：KV Cache 中存储的量化 Key/Value 向量在长序列中累积数值误差，导致注意力分数 (Attention Scores

- **status**: verified
- **level**: L5
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N148

## Claim

量化误差随序列长度累积的机制：KV Cache 中存储的量化 Key/Value 向量在长序列中累积数值误差，导致注意力分数 (Attention Scores) 的 softmax 分布失真，中间位置信息的权重被稀释，加剧 'Lost in the Middle' 效应。

## Corrected Claim

量化误差随序列长度累积的机制：KV Cache 中存储的量化 Key/Value 向量在长序列中累积数值误差，导致注意力分数 (Attention Scores) 的 softmax 分布失真，中间位置信息的权重被稀释，加剧 'Lost in the Middle' 效应。

## Evidence

先验知识/题面给定，逻辑校验通过：量化误差随序列长度线性或累积增长是数值计算的基本性质，且KV Cache误差确实会干扰注意力分布，符合大模型推理的已知机制。
