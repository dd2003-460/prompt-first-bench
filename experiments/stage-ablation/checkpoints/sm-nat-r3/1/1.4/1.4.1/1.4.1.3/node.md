# N130: 在 x_min=4KB 且考虑大小-热度负相关（ρ=-0.3）的工作点下，热门对象（Top 10%）的平均大小 E[S|hot] 低于全局均值 E[S]，冷对象

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N43

## Claim

在 x_min=4KB 且考虑大小-热度负相关（ρ=-0.3）的工作点下，热门对象（Top 10%）的平均大小 E[S|hot] 低于全局均值 E[S]，冷对象（Tail 90%）的平均大小 E[S|cold] 高于全局均值；这种偏差导致基于全局 E[S] 计算的 N_cache 高估了对头部对象的覆盖能力，需分别计算 E[S|hot] 和 E[S|cold] 以修正容量分配。

## Corrected Claim

在 x_min=4KB 且考虑大小-热度负相关（ρ=-0.3）的工作点下，热门对象（Top 10%）的平均大小 E[S|hot] 低于全局均值 E[S]，冷对象（Tail 90%）的平均大小 E[S|cold] 高于全局均值；这种偏差导致基于全局 E[S] 计算的 N_cache 高估了对头部对象的覆盖能力，需分别计算 E[S|hot] 和 E[S|cold] 以修正容量分配。

## Evidence

先验知识/题面给定，逻辑校验通过：负相关（ρ=-0.3）在数学上必然导致条件期望偏离全局均值（E[S|hot] < E[S] < E[S|cold]），且基于全局均值计算缓存容量确实会因忽略分布偏差而高估对头部小对象的覆盖效率，逻辑自洽且符合统计学基本原理。
