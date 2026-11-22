# N53: 对于通用对话和代码生成场景，FP8 精度的质量损失（<1%）通常被视为业务可接受的边界；若业务涉及高精度数学推理或长链逻辑，则必须使用 BF16 或 FP16，

- **status**: degraded
- **level**: L2
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: (root)

## Claim

对于通用对话和代码生成场景，FP8 精度的质量损失（<1%）通常被视为业务可接受的边界；若业务涉及高精度数学推理或长链逻辑，则必须使用 BF16 或 FP16，此时需选择显存 >= 80GB 的硬件（如 A100/H100）或使用多卡拼接。

## Corrected Claim

对于通用对话和代码生成场景，FP8 精度的质量损失（<1%）通常被视为业务可接受的边界；若业务涉及高精度数学推理或长链逻辑，则必须使用 BF16 或 FP16，此时需选择显存 >= 80GB 的硬件（如 A100/H100）或使用多卡拼接。

## Evidence

检索失败: no sources from any channel (all 5 failed)
