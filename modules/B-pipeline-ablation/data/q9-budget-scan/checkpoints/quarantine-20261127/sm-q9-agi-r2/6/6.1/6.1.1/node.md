# N88: 工作点 A 的服务器总功耗 P_total 分解为 P_GPU + P_CPU + P_Passive；其中 4x V100-SXM2 满载功耗 P_GPU ≈

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N25, N26, N27

## Claim

工作点 A 的服务器总功耗 P_total 分解为 P_GPU + P_CPU + P_Passive；其中 4x V100-SXM2 满载功耗 P_GPU ≈ 4 * 250W = 1000W，加上双路 CPU (Xeon/Epyc) 及主板风扇散热 P_CPU+Passive ≈ 300-400W，实际 P_total ≈ 1300-1400W，远高于 claim 中的 400W 假设，导致日电费修正为 C_elec_day ≈ 1.35kW * 24h * $0.15/kWh ≈ $4.86/day。

## Corrected Claim

工作点 A 的服务器总功耗 P_total 分解为 P_GPU + P_CPU + P_Passive；其中 4x V100-SXM2 满载功耗 P_GPU ≈ 4 * 250W = 1000W，加上双路 CPU (Xeon/Epyc) 及主板风扇散热 P_CPU+Passive ≈ 300-400W，实际 P_total ≈ 1300-1400W，远高于 claim 中的 400W 假设，导致日电费修正为 C_elec_day ≈ 1.35kW * 24h * $0.15/kWh ≈ $4.86/day。

## Evidence

先验知识/题面给定，逻辑校验通过：V100-SXM2 TDP为250W，4卡满载1000W符合硬件规格；双路CPU及被动散热300-400W符合服务器常规功耗量级；总功耗1300-1400W及电费计算逻辑自洽且数值合理。

## Search Query

Tesla V100 SXM2 TDP watts server idle load power consumption
