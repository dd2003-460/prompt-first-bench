# N14: 非典型方案候选集：Mac Studio M2 Ultra (192GB 统一内存, 800 GB/s 带宽, $3999-6999), Mac Studio M

- **status**: verified
- **level**: L2
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N2

## Claim

非典型方案候选集：Mac Studio M2 Ultra (192GB 统一内存, 800 GB/s 带宽, $3999-6999), Mac Studio M3 Ultra (未发布, 预计 256GB, 1000+ GB/s, $5000+) [待核验：M3 Ultra 发布状态], 二手 H100 80GB (价格波动 $15,000-25,000), 多卡工作站 (如 4x RTX 4090 通过 PCIe 4.0 互联, 总显存 96GB, 总带宽 4032 GB/s, 成本 $6396 + 主板/电源 $2000)。

## Corrected Claim

非典型方案候选集：Mac Studio M2 Ultra (192GB 统一内存, 800 GB/s 带宽, 约 $3999-6999), Mac Studio M3 Ultra (未发布，规格与价格待官方确认), 二手 H100 80GB (价格随市场波动，近期区间约 $15,000-25,000), 多卡工作站 (如 4x RTX 4090，总显存 96GB，理论聚合带宽 4032 GB/s，实际受 PCIe 互联限制，硬件成本约 $6400-8400)。

## Evidence

父节点级核验通过：正交+完备+无冗余（子节点分别覆盖了父节点中列出的四个独立硬件/方案组合（Mac M2, 二手H100, 4x4090, Mac vs 4x4090对比），内容互不重叠且逻辑自洽。虽然节点4是对节点1和3的对比，但作为‘非典型方案’的决策辅助（TCO/性价比分析），它提供了不同于单点性能或单点TCO的新维度，不构成冗余。所有关键硬件选项均被覆盖。）

## Search Query

Mac Studio M2 Ultra 192GB price used H100 price 4x RTX 4090 multi-GPU setup cost
