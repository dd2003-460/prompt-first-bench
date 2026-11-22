# N80: 多卡方案（2×RTX 4090）的附加系统功耗包括主板、CPU（约100-150W）、RAM（约50W）、散热风扇及PCIe转接卡等，估算附加功耗约为200-3

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N22

## Claim

多卡方案（2×RTX 4090）的附加系统功耗包括主板、CPU（约100-150W）、RAM（约50W）、散热风扇及PCIe转接卡等，估算附加功耗约为200-300W；总功耗 = 2 * 450W + 250W (avg附加) = 1150W。

## Corrected Claim

多卡方案（2×RTX 4090）的附加系统功耗包括主板、CPU（约100-150W）、RAM（约50W）、散热风扇及PCIe转接卡等，估算附加功耗约为200-300W；总功耗 = 2 * 450W + 250W (avg附加) = 1150W。

## Evidence

先验知识/题面给定，逻辑校验通过：2×450W GPU功耗加上200-300W系统附加功耗（CPU/主板/内存等），总功耗1100-1200W，取中值1150W符合物理直觉与工程常识。
