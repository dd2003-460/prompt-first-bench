# N280: S_hot 的量化定义：头部 10% 最热门对象（基于 Pareto(β=0.9) 热度分布）的平均大小，在 ρ=-0.3 线性负相关约束下，S_hot = E

- **status**: verified
- **level**: L4
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N98, N100, N102

## Claim

S_hot 的量化定义：头部 10% 最热门对象（基于 Pareto(β=0.9) 热度分布）的平均大小，在 ρ=-0.3 线性负相关约束下，S_hot = E[S | Top 10%]，其数值取决于 x_min 和 x_max 的截断设定，需通过联合分布数值积分计算。

## Corrected Claim

S_hot 的量化定义：头部 10% 最热门对象（基于 Pareto(β=0.9) 热度分布）的平均大小，在 ρ=-0.3 线性负相关约束下，S_hot = E[S | Top 10%]，其数值取决于 x_min 和 x_max 的截断设定，需通过联合分布数值积分计算。

## Evidence

逻辑推导成立，来源未直接覆盖

## Search Query

Pareto distribution joint correlation average size top 10 percent objects CDN cache
