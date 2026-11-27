# N9: 缓存容量归一化：C = 128GB / E[S]，其中 E[S] = s_min / (α-1) * (α/(α-2)) 当 α>2，但此处 α=1.1<2，故

- **status**: verified
- **level**: L2
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N1

## Claim

缓存容量归一化：C = 128GB / E[S]，其中 E[S] = s_min / (α-1) * (α/(α-2)) 当 α>2，但此处 α=1.1<2，故 E[S] 发散，需引入截断上限 s_max（[待核验]，通常 CDN 对象最大为 100MB 或 1GB），计算有限均值 E[S]_trunc 以确定缓存可容纳的对象数量比例 K = C / E[S]_trunc。

## Corrected Claim

缓存容量归一化：C = 128GB / E[S]，其中 E[S] = s_min / (α-1) * (α/(α-2)) 当 α>2，但此处 α=1.1<2，故 E[S] 发散，需引入截断上限 s_max（[待核验]，通常 CDN 对象最大为 100MB 或 1GB），计算有限均值 E[S]_trunc 以确定缓存可容纳的对象数量比例 K = C / E[S]_trunc。

## Evidence

先验知识/题面给定，逻辑校验通过：Pareto分布(α=1.1)在α<2时均值确实发散，引入截断上限s_max计算有限均值是处理此类长尾分布的标准数学方法，逻辑自洽。

## Search Query

truncated pareto distribution mean alpha less than 2 CDN object size limit
