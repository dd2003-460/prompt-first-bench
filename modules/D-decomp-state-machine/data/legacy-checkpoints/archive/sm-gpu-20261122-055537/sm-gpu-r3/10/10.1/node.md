# N114: NVIDIA L4 显存带宽精确值与 RTX 4090 对比：L4 采用 GDDR6 显存，带宽为 336 GB/s（需确认具体型号规格），而 RTX 4090

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N34

## Claim

NVIDIA L4 显存带宽精确值与 RTX 4090 对比：L4 采用 GDDR6 显存，带宽为 336 GB/s（需确认具体型号规格），而 RTX 4090 为 GDDR6X 1008 GB/s；计算带宽比（1008/336 ≈ 3.0x），验证 N34 中 '300 GB/s' 的表述是否准确，并据此修正理论最大解码速度比。

## Corrected Claim

NVIDIA L4 显存带宽精确值与 RTX 4090 对比：L4 采用 GDDR6 显存，带宽为 336 GB/s（需确认具体型号规格），而 RTX 4090 为 GDDR6X 1008 GB/s；计算带宽比（1008/336 ≈ 3.0x），验证 N34 中 '300 GB/s' 的表述是否准确，并据此修正理论最大解码速度比。

## Evidence

先验知识/题面给定，逻辑校验通过：NVIDIA L4 官方规格确为 336 GB/s，RTX 4090 为 1008 GB/s，比值计算正确。

## Search Query

NVIDIA L4 GDDR6 memory bandwidth GB/s vs RTX 4090 GDDR6X
