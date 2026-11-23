# N43: 对象大小 s 的分布：图片平均 500KB (sigma=200KB)，短视频平均 5MB (sigma=2MB)；总缓存容量 C 固定时，大对象占比越高，可缓

- **status**: verified
- **level**: L3
- **source**: given
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N11

## Claim

对象大小 s 的分布：图片平均 500KB (sigma=200KB)，短视频平均 5MB (sigma=2MB)；总缓存容量 C 固定时，大对象占比越高，可缓存的唯一对象数量越少，导致命中率 H 下降。

## Corrected Claim

对象大小 s 的分布：图片平均 500KB (sigma=200KB)，短视频平均 5MB (sigma=2MB)；总缓存容量 C 固定时，大对象占比越高，可缓存的唯一对象数量越少，导致命中率 H 下降。

## Evidence

先验知识/题面给定，逻辑校验通过：在固定缓存容量C下，对象平均大小s增大，可容纳的唯一对象数量N=C/s必然减少，导致缓存覆盖范围缩小，命中率H下降，符合基本缓存原理。

## Search Query

object size distribution image video CDN cache
