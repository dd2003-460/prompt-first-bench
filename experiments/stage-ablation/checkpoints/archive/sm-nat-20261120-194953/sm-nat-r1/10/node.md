# N27: 完整推导链步骤：1. 计算对象大小分布均值 $E[S]$ 确定单对象平均字节数；2. 确定缓存可容纳的对象数量 $K_{cap} = 128GB / E[S]$

- **status**: verified
- **level**: L2
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: (root)

## Claim

完整推导链步骤：1. 计算对象大小分布均值 $E[S]$ 确定单对象平均字节数；2. 确定缓存可容纳的对象数量 $K_{cap} = 128GB / E[S]$；3. 根据热度分布 $R$ 排序，确定LRU/LFU保留的前 $K_{cap}$ 个对象集合；4. 计算该集合的字节命中率 $H_{base}$；5. 应用更新率折扣 $D_{validity}$ 得到 $H_{eff}$。

## Corrected Claim

完整推导链步骤：1. 计算对象大小分布均值 $E[S]$ 确定单对象平均字节数；2. 确定缓存可容纳的对象数量 $K_{cap} = 128GB / E[S]$；3. 根据热度分布 $R$ 排序，确定LRU/LFU保留的前 $K_{cap}$ 个对象集合；4. 计算该集合的字节命中率 $H_{base}$；5. 应用更新率折扣 $D_{validity}$ 得到 $H_{eff}$。

## Evidence

[rework-angle r1] 逻辑推导成立，来源未直接覆盖

## Search Query

LRU cache hit rate derivation object size distribution
