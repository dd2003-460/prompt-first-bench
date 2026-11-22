# N186: Qwen3-27B 在 AWQ INT4 量化下的 MMLU 分数具体数值或退化百分比，需检索社区量化评测（如 Unsloth, ComfyUI 社区或 Hug

- **status**: degraded
- **level**: L3
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N42

## Claim

Qwen3-27B 在 AWQ INT4 量化下的 MMLU 分数具体数值或退化百分比，需检索社区量化评测（如 Unsloth, ComfyUI 社区或 HuggingFace 量化模型卡）以验证 3-5% 退化的假设。

## Corrected Claim

Qwen3-27B 在 AWQ INT4 量化下的 MMLU 分数具体数值或退化百分比需进一步检索特定评测报告验证；现有来源仅确认该架构支持 AWQ INT4 量化，未提供具体性能退化数据。

## Evidence

[质询]参考来源均指向 'Qwen3.6-27B' 而非 'Qwen3-27B'，存在模型版本混淆风险；且来源摘要仅提及架构与量化技术，未提供具体的 MMLU 分数或 3-5% 退化的实证数据，无法直接验证该具体数值假设。 | 来源 [1][2][3] 主题相关（均为 27B 模型 AWQ INT4 量化），但仅描述技术特性，未提供 MMLU 具体分数或退化百分比，属于间接支持/无直接证据；逻辑上 3-5% 退化符合 INT4 量化常见经验范围，但缺乏来源直接证实。

## Search Query

Qwen3-27B AWQ INT4 MMLU score degradation evaluation

## Retrieval Sources

- {'url': 'https://blog.csdn.net/gitblog_00778/article/details/170514051&rut=8018f922e4a616afe474624869142cbde02a3a82308f40ea736bf74588b132a5', 'type': 'ddg', 'title': '2026旗舰开源多模态大模型Qwen3.6-27B-AWQ-INT4完全解读：27B稠密模型+INT4量化，为什么它能打'}
- {'url': 'https://blog.csdn.net/gitblog_00901/article/details/158275063&rut=bbc3d4eb91a439b4b4328d3b5d6202c67edf5311b5125b0ba2c21899fc3a69c6', 'type': 'ddg', 'title': 'Qwen3.6-27B-AWQ-INT4：27B参数大语言模型实战部署与架构深度解析-CSDN博客'}
- {'url': 'https://devpress.csdn.net/v1/article/detail/158275063&rut=3767b6f9b9258594c5816671101ca39ae2f8f0adaf37fa40e050e8459d36cfc7', 'type': 'ddg', 'title': 'Qwen3.6-27B-AWQ-INT4：27B参数大语言模型实战部署与架构深度解析_霍璟尉-DeepSeek技术社区'}
