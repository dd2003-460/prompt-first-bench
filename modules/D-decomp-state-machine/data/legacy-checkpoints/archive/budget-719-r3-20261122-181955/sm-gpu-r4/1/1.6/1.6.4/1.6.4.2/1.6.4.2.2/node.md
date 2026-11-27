# N622: 512GB DDR5 ECC 内存模块在持续内存访问负载下的平均功耗约为 0.5-0.8W/GB（取决于频率和刷新率），512GB 总内存功耗约为 256W-4

- **status**: verified
- **level**: L5
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N219

## Claim

512GB DDR5 ECC 内存模块在持续内存访问负载下的平均功耗约为 0.5-0.8W/GB（取决于频率和刷新率），512GB 总内存功耗约为 256W-409W，双路 EPYC 服务器整机平均功耗（CPU+内存+其他）约为 832W-1057W，修正 N219 中 600W 的中值估计。

## Corrected Claim

512GB DDR5 ECC 内存模块在持续内存访问负载下的平均功耗约为 0.5-0.8W/GB（取决于频率和刷新率），512GB 总内存功耗约为 256W-409W，双路 EPYC 服务器整机平均功耗（CPU+内存+其他）约为 832W-1057W，修正 N219 中 600W 的中值估计。

## Evidence

先验知识/题面给定，逻辑校验通过：DDR5 ECC 内存功耗量级（0.5-0.8W/GB）符合工程常识，512GB 总功耗及整机功耗估算在逻辑上自洽且量级合理。
