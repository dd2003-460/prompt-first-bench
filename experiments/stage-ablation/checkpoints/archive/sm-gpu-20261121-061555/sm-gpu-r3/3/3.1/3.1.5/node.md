# N76: Qwen3-27B 模型在 W4A16 精度下的 MMLU 准确率下降幅度 ΔAcc = Acc_bf16 - Acc_quant，用于验证是否满足 <1% 的

- **status**: degraded
- **level**: L3
- **source**: search
- **edge_type**: quotient
- **rework_count**: 1
- **parent_ids**: N17

## Claim

Qwen3-27B 模型在 W4A16 精度下的 MMLU 准确率下降幅度 ΔAcc = Acc_bf16 - Acc_quant，用于验证是否满足 <1% 的可接受性阈值 [待核验]

## Corrected Claim

Qwen3-27B 模型在 W4A16 精度下的 MMLU 准确率下降幅度 ΔAcc 需通过实际基准测试验证是否满足 <1% 的可接受性阈值。

## Evidence

[质询]该陈述包含具体的经验性数值结论（ΔAcc < 1%），属于硬件/模型性能指标，无法从第一性原理推导，且缺乏来源支持以确认该特定模型在特定精度下的实际表现。 | 经验事实，逻辑自洽但缺来源支持（检索无可用来源）

## Search Query

Qwen3-27B W4A16 MMLU accuracy drop
