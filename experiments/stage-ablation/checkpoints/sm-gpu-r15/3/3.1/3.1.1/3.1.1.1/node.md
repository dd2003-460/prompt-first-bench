# N124: Qwen3-27B 在 Hugging Face 模型卡中明确标注的总参数量 (Total Parameters) 为 27.8B，该数值包含 Embeddin

- **status**: degraded
- **level**: L4
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N32

## Claim

Qwen3-27B 在 Hugging Face 模型卡中明确标注的总参数量 (Total Parameters) 为 27.8B，该数值包含 Embedding 层和 LM Head 层，是计算显存占用的唯一基准。

## Corrected Claim

Qwen3-27B 的总参数量约为 27.8B（通常包含 Embedding 和 LM Head），是计算显存占用的基准。

## Evidence

[质询]该陈述包含具体的经验数值（27.8B）和特定的文档标注细节（Hugging Face 模型卡明确标注），属于经验事实。参考来源中未包含 Qwen3-27B 的模型卡或相关技术报告，无法直接验证该具体数值及标注方式。 | 经验事实，逻辑自洽但缺来源支持（来源[1]为通用列表，未提供具体参数细节；来源[2]-[4]无关）。

## Search Query

Qwen3-27B huggingface model card total parameters 27.8B

## Retrieval Sources

- {'url': 'https://en.wikipedia.org/wiki/List_of_large_language_models', 'type': None, 'title': 'wiki-full: List of large language models'}
- {'url': 'https://github.com', 'type': None, 'title': 'direct-browser: github.com'}
- {'url': 'http://arxiv.org/abs/2504.07392v6', 'type': 'arxiv', 'title': 'ID-Booth: Identity-consistent Face Generation with Diffusion Models'}
- {'url': 'http://arxiv.org/abs/2509.09729v1', 'type': 'arxiv', 'title': 'MultimodalHugs: Enabling Sign Language Processing in Hugging Face'}
