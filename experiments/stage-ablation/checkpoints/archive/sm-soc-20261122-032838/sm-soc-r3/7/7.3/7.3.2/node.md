# N293: 条件概率计算：在 $D_{trust}=15\%$ 且 $\Delta P=10\%$ 下，买家感知价格 $P_{perc} = P_{low} \cdot (

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N98

## Claim

条件概率计算：在 $D_{trust}=15\%$ 且 $\Delta P=10\%$ 下，买家感知价格 $P_{perc} = P_{low} \cdot (1+D_{trust}) = 0.9 P_{ask} \cdot 1.15 = 1.035 P_{ask}$。若 $P_{threshold} = P_{ref}$ 且 $P_{ask} = 1.2 P_{ref}$，则 $P_{perc} = 1.242 P_{ref}$。计算 $P_{perc} > P_{threshold}$ 的概率为 100%（因为 $1.242 > 1$）。这意味着即使降价10%，加上15%的信任折扣后，买家感知价格仍高于参考价，因此单一信任折扣机制确实无法解释60%无咨询，需引入其他因素（如搜索惯性）。

## Corrected Claim

条件概率计算：在 $D_{trust}=15\%$ 且 $\Delta P=10\%$ 下，买家感知价格 $P_{perc} = P_{low} \cdot (1+D_{trust}) = 0.9 P_{ask} \cdot 1.15 = 1.035 P_{ask}$。若 $P_{threshold} = P_{ref}$ 且 $P_{ask} = 1.2 P_{ref}$，则 $P_{perc} = 1.242 P_{ref}$。计算 $P_{perc} > P_{threshold}$ 的概率为 100%（因为 $1.242 > 1$）。这意味着即使降价10%，加上15%的信任折扣后，买家感知价格仍高于参考价，因此单一信任折扣机制确实无法解释60%无咨询，需引入其他因素（如搜索惯性）。

## Evidence

先验知识/题面给定，逻辑校验通过：数学计算 0.9 * 1.15 = 1.035，1.035 * 1.2 = 1.242，且 1.242 > 1，推导自洽。
