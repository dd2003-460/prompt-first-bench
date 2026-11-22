# N136: W4A16 量化（如 AWQ/GPTQ）中，每 128 个 4-bit 权重共享一个 16-bit 缩放因子（Scale）和 16-bit 零点（Zero-po

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N37

## Claim

W4A16 量化（如 AWQ/GPTQ）中，每 128 个 4-bit 权重共享一个 16-bit 缩放因子（Scale）和 16-bit 零点（Zero-point）；缩放因子带来的额外字节数 = (Total_Params / 128) * 4 bytes。对于 27.1B 参数，额外开销 = (27.1e9 / 128) * 4 ≈ 0.847GB。

## Corrected Claim

W4A16 量化（如 AWQ/GPTQ）中，每 128 个 4-bit 权重共享一个 16-bit 缩放因子（Scale）和 16-bit 零点（Zero-point）；缩放因子带来的额外字节数 = (Total_Params / 128) * 4 bytes。对于 27.1B 参数，额外开销 = (27.1e9 / 128) * 4 ≈ 0.847GB。

## Evidence

先验知识/题面给定，逻辑校验通过：W4A16量化中每128个4-bit权重共享1个16-bit Scale和1个16-bit Zero-point，共32-bit即4字节；27.1e9参数除以128再乘以4字节，计算结果约为0.847GB，量级与逻辑均正确。

## Search Query

AWQ GPTQ 4-bit quantization scale factor memory overhead calculation
