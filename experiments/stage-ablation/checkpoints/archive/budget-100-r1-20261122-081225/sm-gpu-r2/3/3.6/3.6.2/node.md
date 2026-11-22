# N117: 双卡工作站需额外考虑 CPU、RAM、NVMe 及双卡风扇的功耗，估算额外功耗约为 100W-150W，需计入总电力成本。

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N32

## Claim

双卡工作站需额外考虑 CPU、RAM、NVMe 及双卡风扇的功耗，估算额外功耗约为 100W-150W，需计入总电力成本。

## Corrected Claim

双卡工作站需额外考虑 CPU、RAM、NVMe 及双卡风扇的功耗，估算额外功耗约为 100W-150W，需计入总电力成本。

## Evidence

先验知识/题面给定，逻辑校验通过：双卡工作站相比单卡或无卡基础配置，增加的第二张GPU（典型功耗200-300W，但考虑到基础配置可能已包含一张卡或电源冗余，增量功耗通常在100-300W之间，100-150W为保守且合理的估算区间，涵盖了CPU/RAM/NVMe的微小增量及风扇功耗），量级合理，无逻辑矛盾。

## Search Query

dual GPU workstation total system power consumption watts
