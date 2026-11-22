# N631: Qwen3-27B 在 BF16 精度下的 WikiText-103 Perplexity 基线值 (PPL_BF16) 需从 Qwen3 官方技术报告或 Hu

- **status**: degraded
- **level**: L5
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N262

## Claim

Qwen3-27B 在 BF16 精度下的 WikiText-103 Perplexity 基线值 (PPL_BF16) 需从 Qwen3 官方技术报告或 HuggingFace 模型卡获取，若缺失则基于同参数量级 LLM (如 Llama-3-70B) 的 WikiText-103 PPL (约 5.5-6.5) 进行线性插值估算，作为计算 ΔPPL 的分母基准。

## Corrected Claim

Qwen3-27B 在 BF16 精度下的 WikiText-103 Perplexity 基线值 (PPL_BF16) 需从 Qwen3 官方技术报告或 HuggingFace 模型卡获取。若缺失，可参考同参数量级或相近参数量级 LLM（如 Llama-3-70B）的 WikiText-103 PPL 作为定性参考基准，但需注意参数量差异可能导致非线性偏差，不宜直接进行线性插值估算。

## Evidence

[质询]该陈述包含具体的经验数值（Llama-3-70B 的 PPL 约 5.5-6.5）和特定的方法论建议（线性插值估算），属于经验事实。由于检索失败，无法验证 Llama-3-70B 在 WikiText-103 上的具体 PPL 数值是否准确，也无法确认 Qwen3-27B 是否真的缺失该数据或是否适合用 70B 模型进行线性插值（参数量差异较大，非线性关系可能显著）。 | 经验事实，逻辑自洽但缺来源支持。Llama-3-70B 的 PPL 量级在合理范围内，但具体数值和插值方法的适用性无法通过现有来源验证。

## Search Query

Qwen3-27B technical report WikiText-103 perplexity BF16 baseline
