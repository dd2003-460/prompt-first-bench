# N325: RTX 4090 的显存带宽为 1008 GB/s，RTX 5090 为 1792 GB/s，H100 SXM 为 3350 GB/s；在 Decode 敏感场

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N138

## Claim

RTX 4090 的显存带宽为 1008 GB/s，RTX 5090 为 1792 GB/s，H100 SXM 为 3350 GB/s；在 Decode 敏感场景下，单位成本带宽比 (GB/s/$) 决定了性价比，需结合 N106/N122 的价格数据进行计算。

## Corrected Claim

RTX 4090 的显存带宽为 1008 GB/s，RTX 5090 为 1792 GB/s，H100 SXM 为 3350 GB/s；在 Decode 敏感场景下，单位成本带宽比 (GB/s/$) 决定了性价比，需结合 N106/N122 的价格数据进行计算。

## Evidence

先验知识/题面给定，逻辑校验通过：RTX 4090 (1008 GB/s), RTX 5090 (1792 GB/s), H100 SXM (3350 GB/s) 均为公开且稳定的硬件规格参数，数值量级准确；Decode 阶段受显存带宽限制，单位成本带宽比是评估性价比的合理指标。
