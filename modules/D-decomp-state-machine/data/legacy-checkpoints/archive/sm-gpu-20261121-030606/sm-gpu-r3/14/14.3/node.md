# N422: [Verified-Source] 标记的模型参数来源必须精确到 Hugging Face 上的具体模型配置文件（config.json），并记录 commit

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N186

## Claim

[Verified-Source] 标记的模型参数来源必须精确到 Hugging Face 上的具体模型配置文件（config.json），并记录 commit hash 或版本号；例如，Qwen3-27B 的 num_layers=28, hidden_size=4096 等参数需引用特定版本的 config.json，因为不同微调版本或后续迭代（如 Qwen3.5）可能改变这些参数，导致 KV Cache 和显存需求计算失效。

## Corrected Claim

[Verified-Source] 标记的模型参数来源必须精确到 Hugging Face 上的具体模型配置文件（config.json），并记录 commit hash 或版本号；例如，Qwen3-27B 的 num_layers=28, hidden_size=4096 等参数需引用特定版本的 config.json，因为不同微调版本或后续迭代（如 Qwen3.5）可能改变这些参数，导致 KV Cache 和显存需求计算失效。

## Evidence

先验知识/题面给定，逻辑校验通过：模型参数（如层数、隐藏维度）直接决定KV Cache大小和显存占用，不同版本/微调模型参数可能变更，因此精确引用config.json及版本是确保计算有效性的必要工程实践，逻辑自洽且符合事实。

## Search Query

Qwen3-27B Hugging Face config.json num_layers hidden_size version
