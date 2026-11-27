# N39: 计算命中对象集合（前 k_90=11 个）的平均大小 E[S|Hit]：假设热度排名 i 与大小排名 j 存在负相关 ρ=-0.3，采用 Spearman 秩相

- **status**: degraded
- **level**: L3
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N9

## Claim

计算命中对象集合（前 k_90=11 个）的平均大小 E[S|Hit]：假设热度排名 i 与大小排名 j 存在负相关 ρ=-0.3，采用 Spearman 秩相关近似，热对象的大小分布为 S_i ∝ (N - i)^{1/α}（粗略映射），需通过积分或蒙特卡洛模拟计算前 11 个最热对象的平均大小，预期 E[S|Hit] 显著小于 E[S]（例如约为 E[S] 的 50%-70%）

## Corrected Claim

计算命中对象集合（前 k_90=11 个）的平均大小 E[S|Hit]：假设热度排名 i 与大小排名 j 存在负相关，采用 Spearman 秩相关近似，需通过积分或蒙特卡洛模拟计算前 11 个最热对象的平均大小，预期 E[S|Hit] 小于 E[S]。

## Evidence

[质询]该陈述包含具体的经验性数值预测（50%-70%）和特定的统计假设（ρ=-0.3, α参数），这些属于经验事实或特定模型输出，无法从第一性原理严格推导，且缺乏外部来源支持。 | 经验事实，逻辑自洽但缺来源支持（检索无可用来源）

## Search Query

average size of top k objects in Zipf distribution with negative correlation between size and popularity
