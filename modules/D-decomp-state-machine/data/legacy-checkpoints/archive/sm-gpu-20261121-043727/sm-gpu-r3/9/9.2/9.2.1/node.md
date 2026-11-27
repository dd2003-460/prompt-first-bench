# N263: FP8 精度下的 Quality_Score 工作点：假设 Qwen3-27B BF16 MMLU 基线为 0.85 [待核验：需官方评测]，FP8 量化后 M

- **status**: degraded
- **level**: L4
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 1
- **parent_ids**: N98

## Claim

FP8 精度下的 Quality_Score 工作点：假设 Qwen3-27B BF16 MMLU 基线为 0.85 [待核验：需官方评测]，FP8 量化后 MMLU 预估为 0.84 (损失 1%)，则 Quality_Score_FP8 = 0.84/0.85 ≈ 0.988；此值满足 N100 中 Quality_Score >= 0.98 的低损失边界条件，支持 FP8 作为高性价比首选

## Corrected Claim

若Qwen3-27B BF16 MMLU基线为0.85且FP8量化后MMLU预估为0.84，则Quality_Score_FP8约为0.988，满足>=0.98的低损失边界条件；但具体基线分数及量化损失需官方评测确认。

## Evidence

[质询]该陈述依赖于具体的经验事实（Qwen3-27B在MMLU上的具体基线分数及FP8量化后的具体损失率），这些数值无法从第一性原理推导，且参考来源缺失，无法验证0.85和0.84这两个具体数值的准确性。 | 逻辑推导自洽（0.84/0.85≈0.988 > 0.98），但核心数值为经验事实且无来源支持，依据经验事实排除条款降级。

## Search Query

Qwen 27B FP8 quantization MMLU score evaluation quality loss
