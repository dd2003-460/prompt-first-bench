# N418: Qwen3-27B 在 FP8 (E4M3) 量化下的质量损失量化基准：在 MMLU 基准测试上，相比 BF16 基线，准确率下降通常控制在 0.5-1.0% 

- **status**: degraded
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N164

## Claim

Qwen3-27B 在 FP8 (E4M3) 量化下的质量损失量化基准：在 MMLU 基准测试上，相比 BF16 基线，准确率下降通常控制在 0.5-1.0% 以内；在 HumanEval Pass@1 上，下降通常小于 1.5%。若下降超过 2%，则需回退至 INT8 或 BF16，此时显存需求增加，可能排除单卡 24GB/32GB 方案。

## Corrected Claim

Qwen3-27B 在 FP8 (E4M3) 量化下的质量损失通常较小，在 MMLU 和 HumanEval 等基准上相比 BF16 基线的准确率下降通常控制在 1-2% 以内（具体数值取决于量化算法与校准策略）；若下降显著（如超过 2-3%），则需回退至 INT8 或 BF16，此时显存需求增加，可能排除单卡 24GB/32GB 方案。

## Evidence

[质询]具体数值阈值（0.5-1.0% MMLU, <1.5% HumanEval）属于特定模型版本与量化实现的经验性观测数据，不同量化算法（如SmoothQuant, GPTQ, AWQ）及校准集选择会导致显著差异，无法从第一性原理严格推导，且缺乏通用性保证。 | source=knowledge，逻辑自洽（FP8精度高于INT8，损失通常小于INT8；显存需求逻辑正确），但具体百分比为经验事实，无外部来源直接支持，依据经验事实排除条款降级。

## Search Query

Qwen3-27B FP8 quantization MMLU HumanEval accuracy drop
