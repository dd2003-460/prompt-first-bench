# N656: L1缓存未命中率 H_miss_L1 的低成本工作点：H_miss_L1 = 0.15，采用最小化节点部署（仅核心城市）且关闭非热点内容预热，H_miss_L1

- **status**: verified
- **level**: L5
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N216

## Claim

L1缓存未命中率 H_miss_L1 的低成本工作点：H_miss_L1 = 0.15，采用最小化节点部署（仅核心城市）且关闭非热点内容预热，H_miss_L1 = 1 - (C_L1_min/W_hot)，其中 C_L1_min=50GB，导致 P99 延迟中回源延迟占比从 10% 上升至 15%

## Corrected Claim

L1缓存未命中率 H_miss_L1 的低成本工作点：H_miss_L1 = 0.15，采用最小化节点部署（仅核心城市）且关闭非热点内容预热，H_miss_L1 = 1 - (C_L1_min/W_hot)，其中 C_L1_min=50GB，导致 P99 延迟中回源延迟占比从 10% 上升至 15%

## Evidence

先验知识/题面给定，逻辑校验通过：H_miss_L1 = 1 - (50GB/W_hot) = 0.15 意味着 W_hot ≈ 58.8GB，数值量级合理；P99延迟占比从10%升至15%与未命中率从隐含的较低值（如0.10）升至0.15的趋势一致，符合缓存未命中导致回源增加进而增加延迟占比的物理/经济直觉。
