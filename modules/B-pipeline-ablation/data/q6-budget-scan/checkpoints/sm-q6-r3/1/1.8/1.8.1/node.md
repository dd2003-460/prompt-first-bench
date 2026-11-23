# N43: 对象大小 s 的分布：图片平均 500KB (sigma=200KB)，短视频平均 5MB (sigma=2MB)；总缓存容量 C 固定时，大对象占比越高，可缓

- **status**: pending
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

父节点级核验未通过：不完备（子节点详细描述了图片和短视频的大小分布形态，但完全缺失了父节点中关于'总缓存容量C固定时，大对象占比与命中率H关系'这一核心逻辑机制的分解。父节点包含'分布'和'分布对系统性能（命中率）的影响'两部分，子节点仅覆盖了前者。）

## Search Query

object size distribution image video CDN cache
