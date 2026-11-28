# N144: QLoRA 微调总显存需求修正：INT4 权重 (3.375 GB) + LoRA 梯度 (1.74 GB) + Adam 状态 (3.48 GB) + 激活值

- **status**: degraded
- **level**: L4
- **source**: derived
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N39

## Claim

QLoRA 微调总显存需求修正：INT4 权重 (3.375 GB) + LoRA 梯度 (1.74 GB) + Adam 状态 (3.48 GB) + 激活值 (2.0 GB) + 基础开销 (8 GB) = 18.595 GB，低于 64 GB 总显存，证明 QLoRA 在本地硬件上完全可行。

## Corrected Claim

QLoRA 微调总显存需求估算：INT4 权重 (3.375 GB) + LoRA 参数及优化器状态 (<0.5 GB) + 激活值 (2.0 GB) + 基础开销 (8 GB) ≈ 13.9 GB，低于 64 GB 总显存，证明 QLoRA 在本地硬件上可行。

## Evidence

[质询]数值构成存在严重逻辑矛盾：INT4 权重 3.375GB 对应约 8B 参数模型，但 LoRA 梯度 1.74GB 和 Adam 状态 3.48GB 的数值远大于典型 LoRA 微调所需的显存（通常 LoRA 参数仅占原模型 1%-5%，其梯度和优化器状态应远小于 1GB），此处疑似将全量微调的显存占用误标为 LoRA，或数值计算错误。 | 逻辑校验发现内部矛盾：LoRA 组件显存占比异常高，不符合 QLoRA 技术原理（LoRA 仅训练低秩矩阵，显存开销极小），且无外部来源支持该具体数值分解。
