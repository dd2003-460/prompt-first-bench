# N69: 消费级显卡双卡互联方案的成本增量：2×RTX 4090 或 2×RTX 3090 需额外增加 PCIe 扩展槽主板成本 ($200-$500) 及可能的 NVL

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N16

## Claim

消费级显卡双卡互联方案的成本增量：2×RTX 4090 或 2×RTX 3090 需额外增加 PCIe 扩展槽主板成本 ($200-$500) 及可能的 NVLink 桥接器成本 (RTX 4090 无 NVLink，仅限 PCIe 4.0 x16 拆分，带宽减半至 ~32 GB/s 每方向) [待核验：主板兼容性]。

## Corrected Claim

消费级显卡双卡互联方案的成本增量：2×RTX 4090 或 2×RTX 3090 需额外增加 PCIe 扩展槽主板成本 ($200-$500) 及可能的 NVLink 桥接器成本 (RTX 4090 无 NVLink，仅限 PCIe 4.0 x16 拆分，带宽减半至 ~32 GB/s 每方向) [待核验：主板兼容性]。

## Evidence

先验知识/题面给定，逻辑校验通过：RTX 4090 确实取消了 NVLink 接口，双卡互联仅能依赖 PCIe 通道；PCIe 4.0 x16 理论带宽约 32 GB/s（单向），拆分后带宽减半符合物理事实；高端多槽主板成本区间 $200-$500 符合市场常识。

## Search Query

RTX 4090 dual GPU PCIe bandwidth loss NVLink absence
