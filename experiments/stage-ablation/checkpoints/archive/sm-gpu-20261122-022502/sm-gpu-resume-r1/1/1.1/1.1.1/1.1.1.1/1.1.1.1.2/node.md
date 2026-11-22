# N367: Qwen3-27B 的 head_dim 确切值为 128，依据 HuggingFace 官方仓库 Qwen/Qwen3-27B 的 config.json 文

- **status**: degraded
- **level**: L5
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N130, N131, N132

## Claim

Qwen3-27B 的 head_dim 确切值为 128，依据 HuggingFace 官方仓库 Qwen/Qwen3-27B 的 config.json 文件。

## Corrected Claim

Qwen3-27B 的 head_dim 通常为 128，依据 HuggingFace 官方文档中 Qwen3 模型的默认配置说明，但具体需以 Qwen/Qwen3-27B 仓库的 config.json 文件为准。

## Evidence

[质询]参考来源[1]仅提供了Qwen3模型文档中head_dim的默认值（128），并未直接展示Qwen3-27B具体模型的config.json文件内容；来源[2]指向的是Qwen3.8-27B（可能是笔误或不同版本），且摘要未包含配置细节。因此，无法从提供的来源中直接证实Qwen3-27B的head_dim确切为128，尽管这是该系列模型的常见配置。 | 来源[1]间接支持head_dim默认为128，但未直接覆盖Qwen3-27B的具体配置；来源[2]主题相关但摘要未提供配置证据。经验事实，逻辑自洽但缺直接来源支持。

## Search Query

Qwen3-27B config.json head_dim

## Retrieval Sources

- {'url': 'https://huggingface.co/docs/transformers/model_doc/qwen3&rut=c9fc90aaeaad60fbbabac55346c0e79c858e2a8597e4f99bc48b83a3282d4ed7', 'type': 'ddg', 'title': 'Qwen3 · Hugging Face'}
- {'url': 'https://huggingface.co/Qwen/Qwen3.8-27B&rut=9d25219e18a1be7e1ff182cc3d8de44fae124fb6cf28c4acd30a9f864a3aec2a', 'type': 'ddg', 'title': 'Qwen/Qwen3.8-27B · Hugging Face'}
