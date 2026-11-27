# N36: 共享随机源：平台流量分配机制中的随机探索项 ε_traffic，其标准差 σ_ε 决定了算法在确定性GMV排序之外的随机扰动幅度，通常设定为总权重的5%-10%

- **status**: pending
- **level**: L3
- **source**: knowledge
- **edge_type**: stochastic
- **rework_count**: 1
- **parent_ids**: N9

## Claim

共享随机源：平台流量分配机制中的随机探索项 ε_traffic，其标准差 σ_ε 决定了算法在确定性GMV排序之外的随机扰动幅度，通常设定为总权重的5%-10%以平衡探索与利用。

## Corrected Claim

共享随机源：平台流量分配机制中的随机探索项 ε_traffic，其标准差 σ_ε 决定了算法在确定性GMV排序之外的随机扰动幅度，用于平衡探索与利用，具体数值需根据业务场景动态调整。

## Evidence

父节点级核验未通过：不完备（子节点1关注σ_ε的量级估算及其对排序波动的具体影响（阈值验证），子节点2关注ε_traffic的分布假设及其对额外曝光概率的统计验证。两者角度不同（一个侧重绝对量级与排序阈值，一个侧重概率分布与统计显著性），因此正交。但父节点提到“通常设定为总权重的5%-10%以平衡探索与利用”，子节点仅验证了该设定下的具体效应，未覆盖“为何选择5%-10%”或“如何动态调整σ_ε以平衡探索与利用”的关键方面，因此不完备。无冗余。）

## Search Query

platform recommendation algorithm random exploration epsilon traffic allocation
