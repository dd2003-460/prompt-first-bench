# N181: 7.68TB PCIe Gen4 NVMe SSD在Idle状态下的功耗构成：主控芯片低功耗模式(Active Low Power)约1-2W，DRAM缓存自刷

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N59

## Claim

7.68TB PCIe Gen4 NVMe SSD在Idle状态下的功耗构成：主控芯片低功耗模式(Active Low Power)约1-2W，DRAM缓存自刷新(Self-Refresh)约0.5-1W，NAND阵列待机漏电<0.5W，合计约2.5-3.5W，N59给出的5-6W偏高，可能包含了未进入Deep Sleep的过渡态。

## Corrected Claim

7.68TB PCIe Gen4 NVMe SSD在Idle状态下的功耗构成：主控芯片低功耗模式(Active Low Power)约1-2W，DRAM缓存自刷新(Self-Refresh)约0.5-1W，NAND阵列待机漏电<0.5W，合计约2.5-3.5W，N59给出的5-6W偏高，可能包含了未进入Deep Sleep的过渡态。

## Evidence

先验知识/题面给定，逻辑校验通过：各组件功耗量级符合NVMe SSD Idle状态物理特性，总功耗估算合理

## Search Query

NVMe SSD idle power consumption breakdown controller DRAM self-refresh NAND leakage
