# N186: Qwen3-27B 的层数 L 为 64 层，该参数直接决定 KV Cache 总大小的倍数因子，来源为模型 config.json 或 HuggingFace

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N46

## Claim

Qwen3-27B 的层数 L 为 64 层，该参数直接决定 KV Cache 总大小的倍数因子，来源为模型 config.json 或 HuggingFace 官方仓库。

## Corrected Claim

Qwen3-27B 的层数 L 为 64 层，该参数直接决定 KV Cache 总大小的倍数因子，来源为模型 config.json 或 HuggingFace 官方仓库。

## Evidence

先验知识/题面给定，逻辑校验通过

## Search Query

Qwen3-27B config.json num_hidden_layers
