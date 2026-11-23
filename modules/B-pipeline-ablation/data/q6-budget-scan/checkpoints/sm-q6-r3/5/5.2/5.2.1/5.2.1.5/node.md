# N239: 成本增长指数 γ 的物理含义：γ = d(log C_storage) / d(log TTL)，反映存储成本随TTL增加的边际效率；对于NVMe SSD，由于

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N75, N76, N77

## Claim

成本增长指数 γ 的物理含义：γ = d(log C_storage) / d(log TTL)，反映存储成本随TTL增加的边际效率；对于NVMe SSD，由于IOPS和带宽受限，γ通常在0.3-0.7之间，具体值取决于缓存对象的访问频率分布（Zipf指数）

## Corrected Claim

成本增长指数 γ 的物理含义：γ = d(log C_storage) / d(log TTL)，反映存储成本随TTL增加的边际效率；对于NVMe SSD，由于IOPS和带宽受限，γ通常在0.3-0.7之间，具体值取决于缓存对象的访问频率分布（Zipf指数）

## Evidence

先验知识/题面给定，逻辑校验通过
