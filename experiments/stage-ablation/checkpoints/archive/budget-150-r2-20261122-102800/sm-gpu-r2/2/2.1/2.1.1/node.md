# N75: Qwen3-27B 参数量验证：官方文档或 HuggingFace config 确认 total_parameters ≈ 27.18B，其中 Non-Emb

- **status**: degraded
- **level**: L3
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N13

## Claim

Qwen3-27B 参数量验证：官方文档或 HuggingFace config 确认 total_parameters ≈ 27.18B，其中 Non-Embedding 参数 ≈ 26.5B，Embedding+LM_Head ≈ 0.68B (Vocab_size=152K, Hidden=1024, 152000*1024*2 ≈ 311M, 此处需精确计算，若 Vocab 更大则占比不同)。

## Corrected Claim

Qwen3-27B 系列模型参数量约为 27-28B（具体数值因版本和统计口径略有差异，HuggingFace 显示为 28B），其中 Embedding 和 LM Head 参数占比较小，具体分布需查阅对应版本的 config.json 确认。

## Evidence

[质询]来源[1]明确标注模型参数量为28B，与陈述中的27.18B存在显著差异；且来源[1]标题为Qwen3.8-27B，与陈述中的Qwen3-27B版本标识不一致，可能存在版本混淆或参数统计口径（如是否包含Embedding）的差异。 | 来源[1]显示参数量为28B，与27.18B不完全一致但量级接近；来源[2]仅描述架构配置类，未提供具体参数量数值，无法直接支持精确的27.18B及内部参数分布细节。

## Search Query

Qwen3-27B huggingface config total parameters embedding size

## Retrieval Sources

- {'url': 'https://huggingface.co/Qwen/Qwen3.8-27B&rut=f4a8505e184453f0072dff61003e506186593cb27e55fa60c3183db1cee66710', 'type': 'ddg', 'title': 'Qwen/Qwen3.8-27B · Hugging Face'}
- {'url': 'https://huggingface.co/docs/transformers/model_doc/qwen3&rut=8f208edb863f5ffdcaf37c906c848536e8dccd1df308ace10778aff45ed1b42f', 'type': 'ddg', 'title': 'Qwen3 · Hugging Face'}
