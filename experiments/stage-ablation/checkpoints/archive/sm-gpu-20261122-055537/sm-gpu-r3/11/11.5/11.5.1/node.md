# N385: Qwen3-27B 在 MMLU 基准测试上，BF16 基线准确率约为 85-90% [时效待核]，INT4 (AWQ) 量化后准确率通常下降 1-3 个百分点

- **status**: degraded
- **level**: L4
- **source**: search
- **edge_type**: quotient
- **rework_count**: 1
- **parent_ids**: N121

## Claim

Qwen3-27B 在 MMLU 基准测试上，BF16 基线准确率约为 85-90% [时效待核]，INT4 (AWQ) 量化后准确率通常下降 1-3 个百分点，即 Q_score_MMLU = Acc_INT4 / Acc_BF16 ≈ 0.97-0.99。这表明在通用知识任务上，INT4 的质量损失可忽略不计。

## Corrected Claim

Qwen3-27B 在 MMLU 基准测试上，INT4 (AWQ) 量化后的准确率通常略低于 BF16 基线，质量损失较小，具体数值需参考官方技术报告或最新评测数据。

## Evidence

[质询]该陈述包含具体的经验性数值（MMLU基线准确率85-90%及量化损失1-3个百分点），属于硬件/模型性能规格类经验事实，无法从第一性原理推导，且缺乏来源支持。 | 经验事实，逻辑自洽但缺来源支持（检索无可用来源）

## Search Query

Qwen3-27B MMLU benchmark BF16 vs INT4 AWQ accuracy
