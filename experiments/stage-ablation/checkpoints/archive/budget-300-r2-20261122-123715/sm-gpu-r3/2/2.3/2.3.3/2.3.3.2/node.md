# N222: H100 SXM 的 FP8 原生支持使得其单位功耗吞吐量 (TOPS/W) 显著高于 RTX 4090，但需考虑 H100 的 TDP 700W 与 4090

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N62

## Claim

H100 SXM 的 FP8 原生支持使得其单位功耗吞吐量 (TOPS/W) 显著高于 RTX 4090，但需考虑 H100 的 TDP 700W 与 4090 的 450W 差异，以及 H100 需要液冷或高性能风冷基础设施的隐性成本，导致其 TCO 在本地工作站场景中可能因散热和电力复杂度而劣势。

## Corrected Claim

H100 SXM 的 FP8 原生支持使得其单位功耗吞吐量 (TOPS/W) 显著高于 RTX 4090，但需考虑 H100 的 TDP 700W 与 4090 的 450W 差异，以及 H100 需要液冷或高性能风冷基础设施的隐性成本，导致其 TCO 在本地工作站场景中可能因散热和电力复杂度而劣势。

## Evidence

先验知识/题面给定，逻辑校验通过：H100 SXM 确实原生支持 FP8 且 TDP 为 700W，RTX 4090 TDP 为 450W 且不支持原生 FP8（需软件模拟或仅支持 FP16/INT8），H100 的高能效比（TOPS/W）及液冷需求导致的 TCO 劣势符合工程常识与物理直觉。

## Search Query

H100 SXM TCO vs RTX 4090 local workstation power cooling cost
