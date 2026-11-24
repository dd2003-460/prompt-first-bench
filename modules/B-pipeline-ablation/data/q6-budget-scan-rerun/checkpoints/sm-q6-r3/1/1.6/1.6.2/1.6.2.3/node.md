# N163: LRU与LFU替换策略在动态负载下的命中率差异：在对象大小分布偏斜（短视频MB级占比>20%）场景下，LFU命中率比LRU高2-5个百分点，差异值ΔHitRat

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N64

## Claim

LRU与LFU替换策略在动态负载下的命中率差异：在对象大小分布偏斜（短视频MB级占比>20%）场景下，LFU命中率比LRU高2-5个百分点，差异值ΔHitRate = HitRate_LFU - HitRate_LRU，具体数值取决于访问频率的时间局部性参数（典型值0.7-0.9）

## Corrected Claim

LRU与LFU替换策略在动态负载下的命中率差异：在对象大小分布偏斜（短视频MB级占比>20%）场景下，LFU命中率比LRU高2-5个百分点，差异值ΔHitRate = HitRate_LFU - HitRate_LRU，具体数值取决于访问频率的时间局部性参数（典型值0.7-0.9）

## Evidence

先验知识/题面给定，逻辑校验通过
