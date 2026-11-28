# N249: OOM 概率与碎片化的关联：即使理论计算显存未超限，V100 的 HBM 分配器存在内部碎片（Fragmentation），通常预留 5-10% 的安全边际。当

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N86

## Claim

OOM 概率与碎片化的关联：即使理论计算显存未超限，V100 的 HBM 分配器存在内部碎片（Fragmentation），通常预留 5-10% 的安全边际。当理论占用 > 16GB * 0.9 = 14.4GB 时，OOM 概率急剧上升。结合 N94，在 131k 长度下，单序列 KV 约为 262k 的一半，即 ~8.6GB (per card, per seq)，加上权重 3.5GB 和激活 2GB，总计 ~14.1GB，处于 OOM 边缘，实测 OOM 概率 >50% 符合预期。

## Corrected Claim

OOM 概率与碎片化的关联：即使理论计算显存未超限，V100 的 HBM 分配器存在内部碎片（Fragmentation），通常预留 5-10% 的安全边际。当理论占用 > 16GB * 0.9 = 14.4GB 时，OOM 概率急剧上升。结合 N94，在 131k 长度下，单序列 KV 约为 262k 的一半，即 ~8.6GB (per card, per seq)，加上权重 3.5GB 和激活 2GB，总计 ~14.1GB，处于 OOM 边缘，实测 OOM 概率 >50% 符合预期。

## Evidence

先验知识/题面给定，逻辑校验通过：V100 HBM 碎片化导致有效容量低于标称值（约 90% 阈值）符合工程常识；算术推导 8.6+3.5+2=14.1GB 接近 14.4GB 临界值，逻辑自洽。
