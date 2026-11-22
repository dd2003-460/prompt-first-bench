# N167: 中间热度对象对整体命中率折损贡献占比 60% 的量化依据：该群体对象数量占比为 40%（Rank 10%-50%），但其字节流量占比需通过 Pareto(α=1

- **status**: degraded
- **level**: L4
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N57

## Claim

中间热度对象对整体命中率折损贡献占比 60% 的量化依据：该群体对象数量占比为 40%（Rank 10%-50%），但其字节流量占比需通过 Pareto(α=1.1) 大小分布在 Rank 10%-50% 热度区间内的积分计算，预计该区间对象平均大小接近全局均值，导致其字节命中率折损权重 w_byte ≈ 0.4 * (H_byte_mid / H_byte_total)，需通过蒙特卡洛仿真验证 w_byte 是否接近 0.6。

## Corrected Claim

中间热度对象（Rank 10%-50%）数量占比为40%，其字节流量占比及命中率折损权重 w_byte 需通过 Pareto(α=1.1) 分布下的积分计算及蒙特卡洛仿真确定，初步估计 w_byte 可能接近 0.6，但需仿真验证。

## Evidence

[质询]该陈述将‘60%的折损贡献占比’这一经验性结论直接归因于‘对象数量占比40%’及‘平均大小接近全局均值’的简单推导，忽略了Pareto分布下不同热度区间的访问频率（request rate）与对象大小（size）的非线性耦合效应。仅凭数量占比40%和大小接近均值，无法在逻辑上必然推导出字节命中率折损权重w_byte接近0.6，这属于未经验证的假设而非第一性原理推导。 | 经验事实，逻辑自洽但缺来源支持；检索无可用来源，且该数值结论无法从题面条件或第一性原理严格推出，需依赖蒙特卡洛仿真验证。

## Search Query

LRU cache eviction contribution intermediate popularity objects Pareto distribution simulation
