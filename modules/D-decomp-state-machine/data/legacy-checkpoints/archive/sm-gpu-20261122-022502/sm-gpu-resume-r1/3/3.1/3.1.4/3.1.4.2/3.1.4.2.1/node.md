# N676: H200 141GB HBM3e 总带宽为 4.8 TB/s，计算能效比 4.8 TB/s / 700W = 6.857 GB/s/W；H100 80GB HB

- **status**: verified
- **level**: L5
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N209, N210, N211

## Claim

H200 141GB HBM3e 总带宽为 4.8 TB/s，计算能效比 4.8 TB/s / 700W = 6.857 GB/s/W；H100 80GB HBM3 总带宽为 3.35 TB/s，计算能效比 3.35 TB/s / 700W = 4.786 GB/s/W；比值 6.857/4.786 ≈ 1.43，验证了43%提升的数值来源。

## Corrected Claim

H200 141GB HBM3e 总带宽为 4.8 TB/s，计算能效比 4.8 TB/s / 700W = 6.857 GB/s/W；H100 80GB HBM3 总带宽为 3.35 TB/s，计算能效比 3.35 TB/s / 700W = 4.786 GB/s/W；比值 6.857/4.786 ≈ 1.43，验证了43%提升的数值来源。

## Evidence

先验知识/题面给定，逻辑校验通过：H200 (4.8TB/s) 与 H100 (3.35TB/s) 带宽及 700W 功耗符合公开规格，计算过程 4.8/3.35 ≈ 1.433 与 43% 提升一致。

## Search Query

H200 HBM3e bandwidth 4.8TB/s H100 HBM3 bandwidth 3.35TB/s TDP 700W
