# N197: 高溢价商品在 t < 24h 窗口内，Velocity 权重 γ(t) 对总推荐分 W_rec 的贡献占比 S_γ = γ(t) * Velocity / W_

- **status**: degraded
- **level**: L4
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N62

## Claim

高溢价商品在 t < 24h 窗口内，Velocity 权重 γ(t) 对总推荐分 W_rec 的贡献占比 S_γ = γ(t) * Velocity / W_rec，需量化 S_γ 是否足以抵消价格惩罚项 β * δ 的影响（即 S_γ > |β * δ| 的临界条件）。

## Corrected Claim

高溢价商品在 t < 24h 窗口内，Velocity 权重 γ(t) 对总推荐分 W_rec 的贡献占比 S_γ 需量化其是否足以抵消价格惩罚项 β * δ 的影响（即 S_γ > |β * δ| 的临界条件），具体参数与阈值需依据内部实验数据确定。

## Evidence

[质询]该陈述描述的是一个具体的工程实现细节或内部算法逻辑（特定时间窗口、特定变量命名、特定临界条件），属于经验事实/内部规范，无法从第一性原理推导，且缺乏外部来源支持。 | 经验事实，逻辑自洽但缺来源支持

## Search Query

recommendation algorithm velocity weight contribution ratio vs price penalty threshold
