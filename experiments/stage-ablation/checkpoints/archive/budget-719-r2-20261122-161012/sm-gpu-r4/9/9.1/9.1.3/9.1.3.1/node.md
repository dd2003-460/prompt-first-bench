# N685: Qwen3-27B 在 FP8 (E4M3) 精度下的 WikiText-2 Perplexity 实测值需查阅 Qwen 官方技术报告或 HuggingFac

- **status**: degraded
- **level**: L5
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N283

## Claim

Qwen3-27B 在 FP8 (E4M3) 精度下的 WikiText-2 Perplexity 实测值需查阅 Qwen 官方技术报告或 HuggingFace 社区最新评测，当前模型先验估计 PPL 增量为 0.1-0.2（相对于 BF16 基线），若实测 ΔPPL > 0.3 则判定通用对话质量不可接受。

## Corrected Claim

Qwen3-27B 在 FP8 (E4M3) 精度下的 WikiText-2 Perplexity 实测值需查阅 Qwen 官方技术报告或 HuggingFace 社区最新评测。通常 FP8 量化相对于 BF16 基线会有轻微的 PPL 上升，具体增量取决于量化策略，若实测 ΔPPL 显著增大（如 > 0.3）可能影响通用对话质量，需结合具体评测数据判定。

## Evidence

[质询]该陈述包含具体的经验性数值阈值（PPL增量0.1-0.2，判定阈值0.3），属于经验事实而非第一性原理可推导内容，且缺乏官方技术报告或权威评测的直接数据支持，数值可能因具体量化算法（如SmoothQuant, GPTQ等）和校准数据集不同而存在显著差异。 | 经验事实，逻辑自洽但缺来源支持（检索无可用来源，无法验证具体PPL增量数值及阈值合理性）

## Search Query

Qwen3-27B FP8 E4M3 perplexity wikitext-2 benchmark
