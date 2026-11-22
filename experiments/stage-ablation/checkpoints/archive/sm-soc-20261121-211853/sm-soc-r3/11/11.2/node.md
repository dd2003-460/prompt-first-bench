# N185: ‘高价=高质’启发式偏差的量化指标：定义偏差强度 $B_{heuristic} = \frac{\Delta R_{inquiry}}{\Delta P_{hi

- **status**: degraded
- **level**: L4
- **source**: search
- **edge_type**: stochastic
- **rework_count**: 1
- **parent_ids**: N73

## Claim

‘高价=高质’启发式偏差的量化指标：定义偏差强度 $B_{heuristic} = \frac{\Delta R_{inquiry}}{\Delta P_{high}}$，其中 $\Delta R_{inquiry}$ 为高价组（$P > Avg \times 1.15$）相对基准组的咨询率增量，$\Delta P_{high}$ 为溢价幅度；若 $B_{heuristic} > 0.1$，则证明买家将高价随机解读为高质。

## Corrected Claim

‘高价=高质’启发式偏差可通过定义偏差强度 $B_{heuristic} = \frac{\Delta R_{inquiry}}{\Delta P_{high}}$ 进行量化，其中 $\Delta R_{inquiry}$ 为高价组相对基准组的咨询率增量，$\Delta P_{high}$ 为溢价幅度；当 $B_{heuristic}$ 显著大于零（具体阈值需根据具体数据集校准，如 0.1）时，可推断买家存在将高价解读为高质的倾向。

## Evidence

[质询]该陈述定义了一个特定的量化指标 $B_{heuristic}$ 并设定了阈值 0.1，这属于经验性/操作性定义，无法从第一性原理或数学公理中严格推导出来。此外，将‘随机解读’这一认知状态直接等同于‘咨询率增量与溢价幅度的比值大于0.1’存在逻辑跳跃，缺乏因果机制的严谨证明，且阈值 0.1 的选取缺乏普遍公认的统计学或经济学依据。 | 经验事实/操作性定义，逻辑自洽但缺来源支持（本轮检索无可用来源，且该指标非第一性原理可推导，适用经验事实排除条款）

## Search Query

price quality heuristic bias consumer behavior second hand market
