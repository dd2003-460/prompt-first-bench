# N124: Qwen3-27B 在 Hugging Face 模型卡中明确标注的总参数量 (Total Parameters) 为 27.8B，该数值包含 Embeddin

- **status**: pending
- **level**: L4
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N32

## Claim

Qwen3-27B 在 Hugging Face 模型卡中明确标注的总参数量 (Total Parameters) 为 27.8B，该数值包含 Embedding 层和 LM Head 层，是计算显存占用的唯一基准。

## Corrected Claim

Qwen3-27B 的总参数量通常标注为 27.8B（含 Embedding 和 LM Head），是计算显存占用的基准，但需以官方模型卡具体数值为准。

## Evidence

[质询]该陈述属于具体的硬件/模型规格经验事实（参数量数值及显存计算基准），无法从第一性原理推导，且参考来源完全未覆盖该主题，缺乏直接证据支持。 | 参考来源[1][2][3]均与Qwen3模型参数无关，属于无关来源；该事实为经验事实，逻辑自洽但缺来源支持。

## Search Query

Qwen3-27B huggingface model card total parameters 27.8B

## Retrieval Sources

- {'url': 'http://arxiv.org/abs/2504.07392v6', 'type': 'arxiv', 'title': 'ID-Booth: Identity-consistent Face Generation with Diffusion Models'}
- {'url': 'http://arxiv.org/abs/2509.09729v1', 'type': 'arxiv', 'title': 'MultimodalHugs: Enabling Sign Language Processing in Hugging Face'}
- {'url': 'http://arxiv.org/abs/2104.11502v1', 'type': 'arxiv', 'title': 'Learning to Cluster Faces via Transformer'}
