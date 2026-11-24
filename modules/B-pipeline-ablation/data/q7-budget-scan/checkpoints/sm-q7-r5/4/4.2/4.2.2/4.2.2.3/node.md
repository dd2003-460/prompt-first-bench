# N201: 采用12TB SMR HDD方案（N=34盘，RAID6）：物理总容量408TB，有效容量396TB（需微调至400TB则N=35盘），SMR盘在重建大量随机读

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N70

## Claim

采用12TB SMR HDD方案（N=34盘，RAID6）：物理总容量408TB，有效容量396TB（需微调至400TB则N=35盘），SMR盘在重建大量随机读时性能下降30%，有效写带宽降至100-120MB/s/盘。

## Corrected Claim

采用12TB SMR HDD方案（N=34盘，RAID6）：物理总容量408TB，有效容量396TB（需微调至400TB则N=35盘），SMR盘在重建大量随机读时性能下降30%，有效写带宽降至100-120MB/s/盘。

## Evidence

先验知识/题面给定，逻辑校验通过：34*12=408TB，RAID6损失2盘容量后有效容量396TB，计算无误；SMR性能瓶颈描述符合技术常识。
