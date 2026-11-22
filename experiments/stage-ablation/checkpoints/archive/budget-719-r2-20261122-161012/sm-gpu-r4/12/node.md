# N135: Qwen3-27B 在 FP8 (E4M3) 精度下的 Perplexity (PPL) 增加量通常 < 0.1，MMLU 得分下降 < 0.5 个百分点，而 

- **status**: degraded
- **level**: L3
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: (root)

## Claim

Qwen3-27B 在 FP8 (E4M3) 精度下的 Perplexity (PPL) 增加量通常 < 0.1，MMLU 得分下降 < 0.5 个百分点，而 INT4 (AWQ) 精度下 PPL 增加量通常为 0.5-1.5，MMLU 下降 1-3 个百分点 [待核验: 需引用 Qwen3 技术报告或 AWQ 论文具体章节]，这构成了判断精度可接受性的量化底线。

## Corrected Claim

Qwen3-27B 在 FP8 (E4M3) 精度下的性能损失通常显著小于 INT4 (AWQ) 精度，具体量化指标（如 PPL 和 MMLU 下降幅度）需参考 Qwen3 官方技术报告或相关量化评估论文以获取确切数值。

## Evidence

[质询]参考来源仅涉及 Qwen3.8-27B-FP8 的 MathVision 评测提示词格式，完全未包含 PPL 或 MMLU 的具体数值对比，无法支持关于精度损失量化底线（PPL < 0.1, MMLU < 0.5 等）的具体经验数据。 | 逻辑上 FP8 精度高于 INT4，损失更小符合直觉，但具体数值（如 PPL 增加量 0.5-1.5）属于经验事实，参考来源 [1] 与该事实主题无关（仅提及评测提示词），缺乏直接支持，故降级。

## Retrieval Sources

- {'url': 'https://huggingface.co/Qwen/Qwen3.8-27B-FP8&rut=07340cf3a54cad297c9f2b8782c6819a406bad7d8b8a3d2c2339ed2126b742a3', 'type': 'ddg', 'title': 'Qwen/Qwen3.8-27B-FP8 · Hugging Face'}
