# N687: Qwen3-27B 在 FP8 精度下的 HumanEval Pass@1 相对 BF16 基线的绝对下降值 ΔPass@1，模型先验估计为 1-2 个百分点；

- **status**: degraded
- **level**: L5
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N283

## Claim

Qwen3-27B 在 FP8 精度下的 HumanEval Pass@1 相对 BF16 基线的绝对下降值 ΔPass@1，模型先验估计为 1-2 个百分点；需对比 N135 的 INT4 阈值（>5% 不可接受），若 FP8 的 ΔPass@1 < 2% 且显著低于 INT4，则 FP8 在代码生成场景下具备可行性，否则需回退至 BF16。

## Corrected Claim

Qwen3-27B 在 FP8 精度下的 HumanEval Pass@1 相对 BF16 基线的绝对下降值 ΔPass@1 预计较小（通常低于 INT4 的显著下降阈值），具体数值需实测验证；若 ΔPass@1 < 2% 且显著低于 INT4 阈值，则 FP8 在代码生成场景下具备可行性。

## Evidence

[质询]该陈述包含具体的经验性数值估计（FP8精度下降1-2个百分点）及特定模型（Qwen3-27B）的性能表现，属于经验事实，无法从第一性原理推导，且缺乏外部来源支持。 | 经验事实，逻辑自洽但缺来源支持（本轮检索无可用来源）

## Search Query

Qwen3-27B FP8 HumanEval Pass@1 code generation benchmark
