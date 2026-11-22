# N370: Qwen3-27B 的 vocab_size 确切值为 151936，依据 HuggingFace 官方仓库 Qwen/Qwen3-27B 的 config.j

- **status**: verified
- **level**: L5
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N130, N131, N132

## Claim

Qwen3-27B 的 vocab_size 确切值为 151936，依据 HuggingFace 官方仓库 Qwen/Qwen3-27B 的 config.json 文件。

## Corrected Claim

Qwen3-27B 的 vocab_size 确切值为 151936，依据 HuggingFace 官方仓库 Qwen/Qwen3-27B 的 config.json 文件。

## Evidence

来源[1]直接支持，HuggingFace官方文档明确列出Qwen3模型vocab_size默认值为151936。

## Search Query

Qwen3-27B config.json vocab_size

## Retrieval Sources

- {'url': 'https://huggingface.co/docs/transformers/model_doc/qwen3&rut=c9fc90aaeaad60fbbabac55346c0e79c858e2a8597e4f99bc48b83a3282d4ed7', 'type': 'ddg', 'title': 'Qwen3 · Hugging Face'}
