# N364: N34 中 '300 GB/s' 表述验证：N34 若声称 L4 带宽为 300 GB/s，则该数值准确。若声称 336 GB/s 或 320 GB/s，则为错

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N114

## Claim

N34 中 '300 GB/s' 表述验证：N34 若声称 L4 带宽为 300 GB/s，则该数值准确。若声称 336 GB/s 或 320 GB/s，则为错误。修正结论：L4 带宽确为 300 GB/s，RTX 4090 为 1008 GB/s，比值 3.36。

## Corrected Claim

N34 中 '300 GB/s' 表述验证：N34 若声称 L4 带宽为 300 GB/s，则该数值准确。若声称 336 GB/s 或 320 GB/s，则为错误。修正结论：L4 带宽确为 300 GB/s，RTX 4090 为 1008 GB/s，比值 3.36。

## Evidence

先验知识/题面给定，逻辑校验通过：RTX 4090 显存带宽为 1008 GB/s，L4 带宽 300 GB/s，比值 1008/300 = 3.36，数值与逻辑自洽。
