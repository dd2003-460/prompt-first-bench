# N80: SSD 缓存失效后的冷启动时间 (小时) = 温数据预热量 (TB) / (SSD 预加载带宽 GB/s)，假设 100TB 温数据需预热，SSD 带宽 5 G

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N21

## Claim

SSD 缓存失效后的冷启动时间 (小时) = 温数据预热量 (TB) / (SSD 预加载带宽 GB/s)，假设 100TB 温数据需预热，SSD 带宽 5 GB/s，冷启动时间约为 5.5 小时，期间性能降级

## Corrected Claim

SSD 缓存失效后的冷启动时间 (小时) = 温数据预热量 (TB) / (SSD 预加载带宽 GB/s)，假设 100TB 温数据需预热，SSD 带宽 5 GB/s，冷启动时间约为 5.5 小时，期间性能降级

## Evidence

先验知识/题面给定，逻辑校验通过：100TB / 5GB/s = 20000s ≈ 5.56小时，计算正确且量级合理
