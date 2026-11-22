# N204: Qwen3-27B 在 FP8 量化下，MMLU 基准测试准确率相对于 BF16 基线的下降幅度为 0.2-0.5 个百分点（例如 BF16 为 85.0%，F

- **status**: degraded
- **level**: L4
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N66

## Claim

Qwen3-27B 在 FP8 量化下，MMLU 基准测试准确率相对于 BF16 基线的下降幅度为 0.2-0.5 个百分点（例如 BF16 为 85.0%，FP8 为 84.5-84.8%），该数据需从 Qwen 官方技术报告或 Hugging Face 模型卡中获取。

## Corrected Claim

Qwen3-27B 在 FP8 量化下，MMLU 基准测试准确率相对于 BF16 基线通常会有轻微下降，具体幅度需参考 Qwen 官方技术报告或 Hugging Face 模型卡中的实测数据。

## Evidence

[质询]具体数值（0.2-0.5个百分点）及基线分数（85.0%）属于经验事实，缺乏来源支持，且不同量化实现（如SmoothQuant, GPTQ等）可能导致精度损失差异较大，无法仅凭逻辑推导确定具体区间。 | 经验事实，逻辑自洽但缺来源支持（检索无可用来源）

## Search Query

Qwen3-27B FP8 quantization MMLU accuracy drop benchmark
