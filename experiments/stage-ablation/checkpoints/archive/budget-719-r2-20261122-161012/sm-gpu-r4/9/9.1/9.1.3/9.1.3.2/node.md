# N686: Qwen3-27B 在 FP8 精度下的 MMLU 总分相对 BF16 基线的绝对下降值 ΔMMLU，模型先验估计为 0.5-1.5 个百分点；需验证是否低于 

- **status**: degraded
- **level**: L5
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N283

## Claim

Qwen3-27B 在 FP8 精度下的 MMLU 总分相对 BF16 基线的绝对下降值 ΔMMLU，模型先验估计为 0.5-1.5 个百分点；需验证是否低于 N133 定义的 0.5% 相对误差阈值（假设基线 MMLU 为 70%，则允许绝对下降 < 0.35 分，若实测 ΔMMLU > 0.35 则触发质量降级警报）。

## Corrected Claim

Qwen3-27B 在 FP8 精度下的 MMLU 总分相对 BF16 基线的绝对下降值 ΔMMLU 的具体数值需实测验证；若基线 MMLU 为 70%，则 0.5% 相对误差阈值对应允许绝对下降 < 0.35 分，实测值若超过此阈值将触发质量降级警报。

## Evidence

[质询]该陈述包含具体的经验性数值估计（0.5-1.5个百分点）和特定的阈值逻辑，属于经验事实而非第一性原理可推导内容，且缺乏外部来源支持以确认Qwen3-27B在FP8下的实际MMLU下降幅度是否确实落在该区间或是否必然触发警报。 | 经验事实，逻辑自洽但缺来源支持（检索无可用来源）

## Search Query

Qwen3-27B FP8 MMLU score drop vs BF16
