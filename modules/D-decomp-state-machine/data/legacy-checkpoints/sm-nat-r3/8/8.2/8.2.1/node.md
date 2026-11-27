# N274: LRU 驻留时间窗口 T_window 的基准值：在 128GB 缓存和 5000 万日请求负载下，平均驻留时间 T_window ≈ 1 小时，该值由缓存容量

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N96

## Claim

LRU 驻留时间窗口 T_window 的基准值：在 128GB 缓存和 5000 万日请求负载下，平均驻留时间 T_window ≈ 1 小时，该值由缓存容量与对象平均大小决定，是 LRU 驱逐决策的时间阈值。

## Corrected Claim

LRU 驻留时间窗口 T_window 的基准值：在 128GB 缓存和 5000 万日请求负载下，平均驻留时间 T_window ≈ 1 小时，该值由缓存容量与对象平均大小决定，是 LRU 驱逐决策的时间阈值。

## Evidence

先验知识/题面给定，逻辑校验通过：128GB缓存与5000万日请求负载下，平均驻留时间约1小时符合常规缓存容量与流量比例的工程估算量级，无内部矛盾。
