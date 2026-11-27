# N25: LRU有效命中率的折扣系数 $D_{validity}$ 可近似为 $1 - \frac{u \cdot T_{avg}}{1 + u \cdot T_{avg

- **status**: degraded
- **level**: L2
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: (root)

## Claim

LRU有效命中率的折扣系数 $D_{validity}$ 可近似为 $1 - \frac{u \cdot T_{avg}}{1 + u \cdot T_{avg}}$，其中 $T_{avg}$ 是缓存内对象的平均驻留时间。在128GB缓存和5000万请求/天的负载下，需先计算 $T_{avg}$ 再应用此折扣。

## Corrected Claim

LRU有效命中率的折扣系数 $D_{validity}$ 可近似为 $1 - \frac{u \cdot T_{avg}}{1 + u \cdot T_{avg}}$，其中 $T_{avg}$ 是缓存内对象的平均驻留时间。在128GB缓存和5000万请求/天的负载下，需先计算 $T_{avg}$ 再应用此折扣。

## Evidence

检索失败: no sources from any channel (all 5 failed)
