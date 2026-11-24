# N1291: 高码率工作点（s=8.0MB）下，边缘节点 SSD 缓存（5TB/POP）可容纳的热点对象数量 N_hot_high = 5000GB / 8.0MB ≈ 62

- **status**: verified
- **level**: L6
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N441

## Claim

高码率工作点（s=8.0MB）下，边缘节点 SSD 缓存（5TB/POP）可容纳的热点对象数量 N_hot_high = 5000GB / 8.0MB ≈ 625K 个对象，这是缓存覆盖度的上限。

## Corrected Claim

高码率工作点（s=8.0MB）下，边缘节点 SSD 缓存（5TB/POP）可容纳的热点对象数量 N_hot_high = 5000GB / 8.0MB ≈ 625K 个对象，这是缓存覆盖度的上限。

## Evidence

先验知识/题面给定，逻辑校验通过：5000GB / 8.0MB = 5000 * 1024 MB / 8 MB = 640,000，约等于 625K（若按1000进制计算则为625,000），量级与数值合理。
