# N106: 精度损失业务影响函数：定义业务损失函数 L_acc = w * (Acc_base - Acc_quantized)，其中 w 为业务对准确率的敏感度权重 (0

- **status**: degraded
- **level**: L3
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N30

## Claim

精度损失业务影响函数：定义业务损失函数 L_acc = w * (Acc_base - Acc_quantized)，其中 w 为业务对准确率的敏感度权重 (0-1)。需检索 Qwen3-27B 在 MMLU/GSM8K 等基准上，BF16 vs FP8 vs W4 的具体准确率差值 ΔAcc，若 ΔAcc > 阈值 (如 2%)，则 L_acc 显著，需推荐更高精度硬件或接受更低吞吐量。

## Corrected Claim

精度损失业务影响函数：定义业务损失函数 L_acc = w * (Acc_base - Acc_quantized)，其中 w 为业务对准确率的敏感度权重 (0-1)。需评估 Qwen3-27B 在 MMLU/GSM8K 等基准上，BF16 vs FP8 vs W4 的具体准确率差值 ΔAcc，若 ΔAcc 超过业务可接受阈值，则 L_acc 显著，需推荐更高精度硬件或接受更低吞吐量。

## Evidence

[质询]该陈述包含具体的经验性阈值（如 ΔAcc > 2%）和特定模型（Qwen3-27B）在特定量化格式（BF16/FP8/W4）下的具体准确率差值，这些属于经验事实，无法从第一性原理推导，且缺乏来源支持。 | 经验事实，逻辑自洽但缺来源支持（检索无可用来源）

## Search Query

Qwen3 27B quantization accuracy drop FP8 W4 MMLU benchmark
