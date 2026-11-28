# N143: QLoRA 微调中 Adam 优化器状态显存计算：每个可训练参数需 2 个 FP32 状态 (m, v)，故 0.435e9 * 2 * 4 = 3.48 GB

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N39

## Claim

QLoRA 微调中 Adam 优化器状态显存计算：每个可训练参数需 2 个 FP32 状态 (m, v)，故 0.435e9 * 2 * 4 = 3.48 GB。

## Corrected Claim

QLoRA 微调中 Adam 优化器状态显存计算：每个可训练参数需 2 个 FP32 状态 (m, v)，故 0.435e9 * 2 * 4 = 3.48 GB。

## Evidence

先验知识/题面给定，逻辑校验通过：Adam优化器确实需要维护一阶矩(m)和二阶矩(v)两个FP32状态，每个参数占用2*4=8字节，0.435e9 * 8 = 3.48GB，计算无误。
