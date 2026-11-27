# N143: INT4 Group Quantization (Group Size=128) 的 Scale 和 Zero Point 存储开销计算公式：Overhead_

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N53

## Claim

INT4 Group Quantization (Group Size=128) 的 Scale 和 Zero Point 存储开销计算公式：Overhead_GB = (Params / Group_Size) * (Scale_Bits + Zero_Bits) / 8 / 1e9。若 Scale/Zero 均为 FP16 (16 bits)，则 Overhead = (27.18e9 / 128) * (32 / 8) / 1e9 = 0.849 GB

## Corrected Claim

INT4 Group Quantization (Group Size=128) 的 Scale 和 Zero Point 存储开销计算公式：Overhead_GB = (Params / Group_Size) * (Scale_Bits + Zero_Bits) / 8 / 1e9。若 Scale/Zero 均为 FP16 (16 bits)，则 Overhead = (27.18e9 / 128) * (32 / 8) / 1e9 = 0.849 GB

## Evidence

先验知识/题面给定，逻辑校验通过：公式推导正确，数值计算 (27.18e9 / 128) * 4 / 1e9 ≈ 0.849 GB 准确无误。

## Search Query

GPTQ AWQ group quantization scale zero point overhead calculation
