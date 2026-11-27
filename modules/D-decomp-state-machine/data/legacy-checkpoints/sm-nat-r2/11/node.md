# N106: 128GB 缓存容量对应的字节覆盖阈值 S_thresh 约为 2.04KB（即 128GB / 100,000 对象），这意味着只有大小小于 2.04KB 的

- **status**: degraded
- **level**: L3
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: (root)

## Claim

128GB 缓存容量对应的字节覆盖阈值 S_thresh 约为 2.04KB（即 128GB / 100,000 对象），这意味着只有大小小于 2.04KB 的对象才能被全部缓存；若按热度排序保留，LRU 实际能完整保留的对象大小上限需通过累积字节量积分确定，而非简单的平均大小。

## Corrected Claim

128GB 缓存容量对应的字节覆盖阈值 S_thresh 约为 2.04KB（即 128GB / 100,000 对象），这意味着只有大小小于 2.04KB 的对象才能被全部缓存；若按热度排序保留，LRU 实际能完整保留的对象大小上限需通过累积字节量积分确定，而非简单的平均大小。

## Evidence

检索失败: no sources from any channel (all 5 failed)
