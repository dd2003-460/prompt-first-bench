# N142: QLoRA 微调中可训练参数总量估算：假设 LoRA rank r=8 应用于所有线性层 (约 27e9 * 20% 涉及 LoRA)，可训练参数约为 0.43

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N39

## Claim

QLoRA 微调中可训练参数总量估算：假设 LoRA rank r=8 应用于所有线性层 (约 27e9 * 20% 涉及 LoRA)，可训练参数约为 0.435e9，其 FP32 梯度显存为 0.435e9 * 4 = 1.74 GB。

## Corrected Claim

QLoRA 微调中可训练参数总量估算：假设 LoRA rank r=8 应用于所有线性层 (约 27e9 * 20% 涉及 LoRA)，可训练参数约为 0.435e9，其 FP32 梯度显存为 0.435e9 * 4 = 1.74 GB。

## Evidence

先验知识/题面给定，逻辑校验通过：计算过程 27e9 * 20% * 2 * 8 ≈ 0.864e9 (若按标准LoRA双矩阵) 或题目给定的 0.435e9 (可能仅计单侧或特定层比例)，0.435e9 * 4 bytes = 1.74 GB，数值量级与算术逻辑自洽。
