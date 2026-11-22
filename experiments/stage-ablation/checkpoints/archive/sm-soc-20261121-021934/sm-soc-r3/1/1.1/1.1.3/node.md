# N24: 下游投影2：成交周期 T_deal 的随机扰动项 δT = β_noise * |ε_i|，其中 β_noise 为买家对价格异常值的敏感度系数（通常 β_no

- **status**: pending
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N5

## Claim

下游投影2：成交周期 T_deal 的随机扰动项 δT = β_noise * |ε_i|，其中 β_noise 为买家对价格异常值的敏感度系数（通常 β_noise > 0），当 |ε_i| 超过买家阈值 θ_buyer（如 2σ_ε）时，δT 呈指数增长，解释了部分高挂价商品虽未成交但咨询量低的现象。

## Corrected Claim

下游投影2：成交周期 T_deal 的随机扰动项 δT = β_noise * |ε_i|，其中 β_noise 为买家对价格异常值的敏感度系数（通常 β_noise > 0），当 |ε_i| 超过买家阈值 θ_buyer（如 2σ_ε）时，δT 呈指数增长，解释了部分高挂价商品虽未成交但咨询量低的现象。

## Evidence

父节点级核验未通过：不完备（子节点之间存在逻辑依赖（子节点2依赖子节点1定义的阈值），但主题不重叠，正交性基本成立。然而，父节点中明确提到的核心参数 β_noise（敏感度系数）在两个子节点中均未给出其量化、估计方法或定义，导致关键方面覆盖不全（不完备）。）

## Search Query

price sensitivity buyer decision time threshold
