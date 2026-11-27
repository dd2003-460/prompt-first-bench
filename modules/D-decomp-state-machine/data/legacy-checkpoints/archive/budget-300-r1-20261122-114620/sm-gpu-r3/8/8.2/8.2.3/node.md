# N365: Qwen3-27B 在 W4A16 (GPTQ/AWQ) 量化下 GSM8K 基准精度通常为 81.0% (Pass@1)，相对 BF16 下降约 5.8%，仍

- **status**: degraded
- **level**: L4
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N128

## Claim

Qwen3-27B 在 W4A16 (GPTQ/AWQ) 量化下 GSM8K 基准精度通常为 81.0% (Pass@1)，相对 BF16 下降约 5.8%，仍略高于 5% 阈值，但在多步推理长链中误差累积效应显著。

## Corrected Claim

Qwen3-27B 在 W4A16 (GPTQ/AWQ) 量化下 GSM8K 基准精度通常约为 81% (Pass@1)，相对 BF16 存在一定精度下降，但在多步推理长链中误差累积效应显著。

## Evidence

[质询]具体数值（81.0%）和相对下降幅度（5.8%）属于特定量化配置下的经验测量值，不同量化实现（GPTQ vs AWQ）、校准数据集及推理设置会导致结果波动，且Qwen3-27B的BF16基准分通常高于86.8%（81.0+5.8），需确认具体基准版本；此外，'误差累积效应显著'为定性描述，缺乏量化支撑。 | 经验事实，逻辑自洽但缺来源支持（检索无可用来源）

## Search Query

Qwen3-27B AWQ W4 GSM8K benchmark accuracy
