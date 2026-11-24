# N110: Dirichlet 分布参数 α_i 的先验估计：基于 N39 的一手数据，设 α_i = 10 × geo_share_prior_i，其中 geo_shar

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N33

## Claim

Dirichlet 分布参数 α_i 的先验估计：基于 N39 的一手数据，设 α_i = 10 × geo_share_prior_i，其中 geo_share_prior_i 为 N39 中确定的基准占比；例如，若某核心省份占比 0.15，则 α_i = 1.5；该参数化确保采样出的 geo_share 分布围绕先验均值波动，且总和为 1，避免极端不均衡的采样点。

## Corrected Claim

Dirichlet 分布参数 α_i 的先验估计：基于 N39 的一手数据，设 α_i = 10 × geo_share_prior_i，其中 geo_share_prior_i 为 N39 中确定的基准占比；例如，若某核心省份占比 0.15，则 α_i = 1.5；该参数化确保采样出的 geo_share 分布围绕先验均值波动，且总和为 1，避免极端不均衡的采样点。

## Evidence

父节点级核验通过：正交+完备+无冗余（三个子节点分别聚焦于参数计算与方差结构、边界条件与截断策略、以及采样偏差验证，逻辑上分别对应‘参数定义’、‘约束处理’和‘数值验证’，彼此正交且无重叠。父节点提到的‘避免极端不均衡’在子节点2中得到了具体的技术实现（截断/调整下限），‘围绕先验均值波动’在子节点1（方差）和子节点3（偏差验证）中得到了完整覆盖。没有发现冗余内容，各子节点均为独立的逻辑步骤。）
