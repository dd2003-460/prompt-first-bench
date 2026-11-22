# N332: 2×RTX 3090 方案中，若主板原生提供 2 个 PCIe x16 插槽且物理间距足够，则无需额外购买 PCIe 扩展卡，互联成本为 $0；RTX 3090

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N95, N96, N97

## Claim

2×RTX 3090 方案中，若主板原生提供 2 个 PCIe x16 插槽且物理间距足够，则无需额外购买 PCIe 扩展卡，互联成本为 $0；RTX 3090 为 3 槽设计，需确认主板插槽间距是否支持双卡安装

## Corrected Claim

2×RTX 3090 方案中，若主板原生提供 2 个 PCIe x16 插槽且物理间距足够，则无需额外购买 PCIe 扩展卡，互联成本为 $0；RTX 3090 为 3 槽设计，需确认主板插槽间距是否支持双卡安装

## Evidence

先验知识/题面给定，逻辑校验通过：RTX 3090 确为 3 槽设计，双卡安装需主板支持且间距足够，若满足条件则无需扩展卡，成本为 0 符合逻辑。
