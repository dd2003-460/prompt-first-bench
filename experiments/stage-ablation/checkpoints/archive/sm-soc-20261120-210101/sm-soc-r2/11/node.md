# N116: 最小干预策略‘价格偏离度可视化’的量化设计：在商品列表页展示‘偏离近期均价 X%’标签。干预强度参数 η_display 定义为标签的视觉显著性（字号、颜色对比

- **status**: degraded
- **level**: L3
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: (root)

## Claim

最小干预策略‘价格偏离度可视化’的量化设计：在商品列表页展示‘偏离近期均价 X%’标签。干预强度参数 η_display 定义为标签的视觉显著性（字号、颜色对比度）。假设 η_display = 0.8（高显著性）时，买家对高挂价的容忍度 ΔTol 下降 40%，即新的容忍阈值 θ_stop_new = θ_stop_old * (1 - 0.4)。

## Corrected Claim

最小干预策略‘价格偏离度可视化’的量化设计：在商品列表页展示‘偏离近期均价 X%’标签。干预强度参数 η_display 定义为标签的视觉显著性（字号、颜色对比度）。假设 η_display = 0.8（高显著性）时，买家对高挂价的容忍度 ΔTol 下降 40%，即新的容忍阈值 θ_stop_new = θ_stop_old * (1 - 0.4)。

## Evidence

检索失败: no sources from any channel (all 5 failed)
