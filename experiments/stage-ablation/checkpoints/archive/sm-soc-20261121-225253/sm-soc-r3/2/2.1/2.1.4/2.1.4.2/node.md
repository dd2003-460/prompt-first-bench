# N76: GMV最大化目标下平台对高挂价商品的曝光偏置机制：平台优化目标函数 $\max \sum P_{ask} \times P_{deal|ask} \times 

- **status**: degraded
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N28

## Claim

GMV最大化目标下平台对高挂价商品的曝光偏置机制：平台优化目标函数 $\max \sum P_{ask} \times P_{deal|ask} \times E$，其中 $P_{deal|ask}$ 随 $P_{ask}$ 上升而下降（弹性 $\eta_{demand} < 0$），但在 $P_{ask}$ 处于最优区间 $[P_{mkt}, P_{mkt} \times 1.25]$ 时，边际收益 $\frac{\partial GMV}{\partial P_{ask}} > 0$，导致算法主动给予该区间商品更高曝光权重 $W_{exp}$，具体表现为 $W_{exp} = W_{base} \times (1 + \gamma \times \frac{P_{ask}-P_{mkt}}{P_{mkt}})$，其中 $\gamma$ 为平台激励系数，经验值约 0.1-0.2。

## Corrected Claim

在GMV最大化目标下，平台算法倾向于对处于合理溢价区间（高于市场价但低于成交概率急剧下降阈值）的商品给予更高曝光权重，以平衡单价提升与成交概率下降之间的边际收益。

## Evidence

[质询]该陈述包含具体的经验参数（如最优区间上限1.25倍、激励系数γ=0.1-0.2）及特定的线性曝光权重公式，这些属于平台内部算法的黑盒经验事实，无法从第一性原理严格推导，且不同平台或时期参数可能不同，存在过度具体化导致失真的风险。 | source=knowledge，逻辑自洽（GMV最大化下存在权衡区间符合经济学直觉），但具体数值参数（1.25, 0.1-0.2）缺乏通用理论支撑，属经验事实，降级为定性表述。

## Search Query

platform GMV optimization pricing strategy exposure bias
