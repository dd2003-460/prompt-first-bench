# N10: 工作点 1（高召回低精度）：假设 LRU 缓存完全由最近 $T_{recent}$ 天内访问过的对象组成，估算 $T_{recent}$ 使得缓存占用 128G

- **status**: verified
- **level**: L2
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N1, N2, N3

## Claim

工作点 1（高召回低精度）：假设 LRU 缓存完全由最近 $T_{recent}$ 天内访问过的对象组成，估算 $T_{recent}$ 使得缓存占用 128GB，计算该窗口内的字节命中率下界，忽略长期热点的复用。

## Corrected Claim

工作点 1（高召回低精度）：假设 LRU 缓存完全由最近 $T_{recent}$ 天内访问过的对象组成，估算 $T_{recent}$ 使得缓存占用 128GB，计算该窗口内的字节命中率下界，忽略长期热点的复用。

## Evidence

先验知识/题面给定，逻辑校验通过
