# N99: FP8 量化相比 BF16 的困惑度（Perplexity）增加幅度通常在 0.5%-1.5% 之间，对于 Qwen3-27B 而言，若 BF16 基准困惑度为

- **status**: degraded
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N21

## Claim

FP8 量化相比 BF16 的困惑度（Perplexity）增加幅度通常在 0.5%-1.5% 之间，对于 Qwen3-27B 而言，若 BF16 基准困惑度为 8.2，FP8 量化后的困惑度预计约为 8.24-8.30，质量损失在大多数通用任务中可忽略不计。

## Corrected Claim

FP8 量化相比 BF16 通常能保持较高的模型精度，困惑度增加幅度通常较小（具体数值依模型和任务而异），对于大语言模型而言，在大多数通用任务中质量损失通常可忽略不计。

## Evidence

[质询]该陈述包含具体的经验性数值（0.5%-1.5% 的困惑度增加幅度）和特定模型（Qwen3-27B）的基准困惑度（8.2），这些属于经验事实而非第一性原理可推导内容。虽然 FP8 量化通常比 BF16 损失小，但具体幅度高度依赖于模型架构、训练数据分布及量化算法（如 SmoothQuant, GPTQ 等），0.5%-1.5% 并非普适常数，且 Qwen3-27B 的 BF16 基准困惑度 8.2 需具体验证，不同评测集下数值差异较大。 | 经验事实，逻辑自洽但缺来源支持。FP8 量化通常优于 BF16 的精度损失是已知趋势，但具体百分比范围和特定模型基准值属于经验数据，无外部来源直接支持，且不同场景下波动较大，故降级为定性表述。

## Search Query

FP8 quantization perplexity degradation LLM benchmark
