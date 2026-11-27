# N104: Qwen3-27B 的层数 (num_hidden_layers) 为 64，需通过模型 config.json 或 HuggingFace 仓库元数据确认，此

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N33

## Claim

Qwen3-27B 的层数 (num_hidden_layers) 为 64，需通过模型 config.json 或 HuggingFace 仓库元数据确认，此为计算 KV Cache 的基础参数

## Corrected Claim

Qwen3-27B 的层数 (num_hidden_layers) 为 64，需通过模型 config.json 或 HuggingFace 仓库元数据确认，此为计算 KV Cache 的基础参数

## Evidence

先验知识/题面给定，逻辑校验通过

## Search Query

Qwen3-27B config.json num_hidden_layers
