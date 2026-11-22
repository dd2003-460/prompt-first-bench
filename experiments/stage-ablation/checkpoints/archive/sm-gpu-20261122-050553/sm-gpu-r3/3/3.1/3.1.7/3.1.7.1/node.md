# N213: Qwen3-27B 使用 GPTQ (INT8, 1024 samples) 量化后在 MMLU 基准上的准确率变化：基线 BF16 准确率约 82-84% [

- **status**: degraded
- **level**: L4
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N69

## Claim

Qwen3-27B 使用 GPTQ (INT8, 1024 samples) 量化后在 MMLU 基准上的准确率变化：基线 BF16 准确率约 82-84% [待核验具体版本]，GPTQ INT8 后准确率下降约 0.5-1.5 个百分点，即 81-83.5%，低于 2% 容忍阈值。

## Corrected Claim

Qwen3-27B 使用 GPTQ (INT8) 量化后在 MMLU 基准上的准确率通常会有轻微下降（约 0.5-1.5 个百分点），具体数值取决于基线版本与量化实现细节。

## Evidence

[质询]具体数值（基线82-84%及下降0.5-1.5pp）属于特定模型版本与量化配置下的经验事实，缺乏来源支持，且不同量化实现或数据集版本可能导致数值波动，无法仅凭逻辑推导确定具体区间。 | 经验事实，逻辑自洽（INT8量化通常导致轻微精度损失）但缺来源支持，且检索无可用来源。

## Search Query

Qwen3-27B GPTQ INT8 MMLU accuracy benchmark
