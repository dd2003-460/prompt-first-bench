# N205: Qwen3-27B 在 FP8 量化下，GSM8K 基准测试准确率相对于 BF16 基线的下降幅度为 0.5-1.0 个百分点（例如 BF16 为 92.0%，

- **status**: degraded
- **level**: L4
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N66

## Claim

Qwen3-27B 在 FP8 量化下，GSM8K 基准测试准确率相对于 BF16 基线的下降幅度为 0.5-1.0 个百分点（例如 BF16 为 92.0%，FP8 为 91.0-91.5%），数学推理任务对量化更敏感。

## Corrected Claim

Qwen3-27B 在 FP8 量化下，GSM8K 基准测试准确率相对于 BF16 基线通常会有轻微下降（约 0.5-1.0 个百分点），数学推理任务对量化精度较为敏感。

## Evidence

[质询]具体数值（92.0%基线及0.5-1.0pp下降幅度）属于特定模型版本的经验事实，缺乏来源支持，且不同量化实现（如SmoothQuant vs 原生FP8）可能导致结果差异，存在口径混淆风险。 | 经验事实，逻辑自洽但缺来源支持（检索无可用来源）

## Search Query

Qwen3-27B FP8 quantization GSM8K accuracy drop benchmark
