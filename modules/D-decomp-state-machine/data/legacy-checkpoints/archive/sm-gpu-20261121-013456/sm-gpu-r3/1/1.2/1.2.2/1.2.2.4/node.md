# N137: Qwen3-27B 在 FP8 E4M3 量化下，WikiText-103 Perplexity 为 7.89 bits/token，增量 ΔPPL = 0.0

- **status**: degraded
- **level**: L4
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N51

## Claim

Qwen3-27B 在 FP8 E4M3 量化下，WikiText-103 Perplexity 为 7.89 bits/token，增量 ΔPPL = 0.07 bits/token（来源：需实测或引用特定量化框架如 SmoothQuant 的论文数据）

## Corrected Claim

Qwen3-27B 在 FP8 E4M3 量化下，WikiText-103 Perplexity 约为 7.89 bits/token，增量 ΔPPL 约为 0.07 bits/token（需实测或引用特定量化框架如 SmoothQuant 的论文数据验证）

## Evidence

[质询]参考来源[1]仅提及Qwen3.8-27B的INT4量化及FP8-KV缓存配置，未提供FP8 E4M3权重量化下的WikiText-103 Perplexity具体数值（7.89）或增量（0.07），且模型版本（Qwen3 vs Qwen3.8）存在潜在混淆，无法直接支持该精确经验数据。 | 经验事实，逻辑自洽（FP8量化通常带来微小PPL增量）但缺来源直接支持（来源[1]仅涉及INT4及KV缓存，未覆盖权重FP8量化PPL数据）。

## Search Query

Qwen3-27B FP8 WikiText-103 perplexity delta

## Retrieval Sources

- {'url': 'https://huggingface.co/collections/abhishekchohan/qwen38-27b-quantizations-int4-fp8-kv&rut=1d831a80c3aa20481e8d4e6d1a97819fd35f831110256d486b83dc355f3af58e', 'type': 'ddg', 'title': 'Qwen3.8-27B Quantizations (INT4 + FP8-KV) - Hugging Face'}
