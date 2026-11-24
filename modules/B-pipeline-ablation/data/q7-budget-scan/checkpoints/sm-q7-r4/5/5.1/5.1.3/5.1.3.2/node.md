# N324: HDD 层 8,000 IOPS 的计算细节：40 块 HDD * 200 IOPS/盘 = 8,000 IOPS，此处 200 IOPS/盘 为 4KB 随机

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N119

## Claim

HDD 层 8,000 IOPS 的计算细节：40 块 HDD * 200 IOPS/盘 = 8,000 IOPS，此处 200 IOPS/盘 为 4KB 随机读的乐观估计（典型值 100-150），若取 150 IOPS/盘，总 HDD IOPS 为 6,000，需结合 SSD 缓存命中率重新评估总负载

## Corrected Claim

HDD 层 8,000 IOPS 的计算细节：40 块 HDD * 200 IOPS/盘 = 8,000 IOPS，此处 200 IOPS/盘 为 4KB 随机读的乐观估计（典型值 100-150），若取 150 IOPS/盘，总 HDD IOPS 为 6,000，需结合 SSD 缓存命中率重新评估总负载

## Evidence

先验知识/题面给定，逻辑校验通过：40*200=8000及40*150=6000计算正确，200 IOPS/盘作为4KB随机读的乐观估计符合HDD性能常识（典型值100-150），逻辑自洽且数值量级合理。
