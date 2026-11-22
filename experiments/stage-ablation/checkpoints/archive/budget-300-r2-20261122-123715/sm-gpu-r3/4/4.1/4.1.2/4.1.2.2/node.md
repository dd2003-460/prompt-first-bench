# N293: Qwen3-27B 在 FP8 (E4M3) 精度下的实测质量基准数据：需确认 FP8 量化在 27B 规模模型上的困惑度增量 ΔPPL 是否严格小于 0.1，

- **status**: degraded
- **level**: L4
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N85, N86, N87

## Claim

Qwen3-27B 在 FP8 (E4M3) 精度下的实测质量基准数据：需确认 FP8 量化在 27B 规模模型上的困惑度增量 ΔPPL 是否严格小于 0.1，以及 MMLU 准确率保持率是否 >99%，作为高保真低精度方案的可行性依据。

## Corrected Claim

Qwen3-27B 在 FP8 (E4M3) 精度下的实测质量基准数据需进一步验证：需确认 FP8 量化在 27B 规模模型上的困惑度增量 ΔPPL 是否严格小于 0.1，以及 MMLU 准确率保持率是否 >99%，作为高保真低精度方案的可行性依据。

## Evidence

[质询]该陈述包含具体的经验性数值阈值（ΔPPL < 0.1, MMLU > 99%），属于特定模型在特定精度下的实测性能指标，无法从第一性原理推导，且缺乏来源支持以确认这些具体数值是否准确反映了 Qwen3-27B 的实际表现。 | 经验事实，逻辑自洽但缺来源支持（检索无可用来源）

## Search Query

Qwen3-27B FP8 E4M3 quantization perplexity delta MMLU accuracy retention
