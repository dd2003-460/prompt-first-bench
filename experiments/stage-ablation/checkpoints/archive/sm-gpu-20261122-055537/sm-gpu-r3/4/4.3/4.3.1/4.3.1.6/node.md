# N238: 修正 N70 中的溢价系数 K_infra：基于 N123-N127 的分解，C_cool_datacenter ≈ $450-1500/年，C_cool_co

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N69, N70, N71

## Claim

修正 N70 中的溢价系数 K_infra：基于 N123-N127 的分解，C_cool_datacenter ≈ $450-1500/年，C_cool_consumer ≈ $10-20/年，K_infra 实际范围约为 22-150 倍，而非原估的 10-40 倍。此差异主要源于 H100 SXM 对专用供电和散热硬件的刚性依赖，而非单纯的风扇功耗差异。

## Corrected Claim

修正 N70 中的溢价系数 K_infra：基于 N123-N127 的分解，C_cool_datacenter ≈ $450-1500/年，C_cool_consumer ≈ $10-20/年，K_infra 实际范围约为 22-150 倍，而非原估的 10-40 倍。此差异主要源于 H100 SXM 对专用供电和散热硬件的刚性依赖，而非单纯的风扇功耗差异。

## Evidence

先验知识/题面给定，逻辑校验通过：数据中心冷却成本（$450-1500/年）与消费级（$10-20/年）的量级差异符合工程常识，比值22-150倍在数学上自洽，且归因于基础设施刚性依赖符合物理直觉。
