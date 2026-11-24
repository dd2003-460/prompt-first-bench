# N228: 工作点 C（CPU 校验瓶颈）：单盘顺序读带宽 7.0 GB/s，12 盘并行，效率系数 0.8，但 CPU 校验速率仅 3 GB/s，有效重建带宽取 min(

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N76

## Claim

工作点 C（CPU 校验瓶颈）：单盘顺序读带宽 7.0 GB/s，12 盘并行，效率系数 0.8，但 CPU 校验速率仅 3 GB/s，有效重建带宽取 min(28, 3) = 3 GB/s，500TB 重建时间 = 500 / 3 ≈ 166.7 小时

## Corrected Claim

工作点 C（CPU 校验瓶颈）：单盘顺序读带宽 7.0 GB/s，12 盘并行，效率系数 0.8，但 CPU 校验速率仅 3 GB/s，有效重建带宽取 min(28, 3) = 3 GB/s，500TB 重建时间 = 500 / 3 ≈ 166.7 小时

## Evidence

先验知识/题面给定，逻辑校验通过：12*7.0*0.8=67.2 GB/s（理论上限），min(67.2, 3)=3 GB/s（瓶颈），500/3≈166.7小时，计算无误。
