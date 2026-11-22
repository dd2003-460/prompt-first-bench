# N438: FP8 (E4M3) 精度下 Qwen3-27B 在 GSM8K 基准测试上的准确率绝对值及相对于 BF16 基线的下降幅度（Delta_GSM8K），用于计算

- **status**: degraded
- **level**: L4
- **source**: search
- **edge_type**: quotient
- **rework_count**: 1
- **parent_ids**: N141

## Claim

FP8 (E4M3) 精度下 Qwen3-27B 在 GSM8K 基准测试上的准确率绝对值及相对于 BF16 基线的下降幅度（Delta_GSM8K），用于计算 QF_GSM8K = Acc_FP8 / Acc_BF16，以验证数学推理任务上的质量保持率。

## Corrected Claim

FP8 (E4M3) 精度下 Qwen3-27B 在 GSM8K 基准测试上的准确率通常接近 BF16 基线，具体绝对值及下降幅度需查阅特定量化实验报告。

## Evidence

[质询]该陈述包含具体的经验性数值（Qwen3-27B在GSM8K上的FP8与BF16准确率及差值），属于硬件/模型性能经验事实，无法从第一性原理推导，且当前无可用来源支持具体数值。 | 经验事实，逻辑自洽但缺来源支持

## Search Query

Qwen3-27B FP8 GSM8K accuracy benchmark comparison BF16
