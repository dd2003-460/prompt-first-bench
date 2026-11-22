# N68: 负面外部性的下限估计：即使仅影响5%卖家，若这5%卖家贡献了平台20%的GMV（基于幂律分布假设），则干预导致的潜在GMV损失 $\Delta GMV = 0.

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N25

## Claim

负面外部性的下限估计：即使仅影响5%卖家，若这5%卖家贡献了平台20%的GMV（基于幂律分布假设），则干预导致的潜在GMV损失 $\Delta GMV = 0.05 \times N_{sellers} \times 0.2 \times AvgOrderValue$。需核验高溢价卖家是否真的贡献了不成比例的GMV，若未贡献，则帕累托改进的‘伤害’可忽略。

## Corrected Claim

负面外部性的下限估计：即使仅影响5%卖家，若这5%卖家贡献了平台20%的GMV（基于幂律分布假设），则干预导致的潜在GMV损失 $\Delta GMV = 0.05 \times N_{sellers} \times 0.2 \times AvgOrderValue$。需核验高溢价卖家是否真的贡献了不成比例的GMV，若未贡献，则帕累托改进的‘伤害’可忽略。

## Evidence

父节点级核验通过：正交+完备+无冗余（子节点分别对应参数估计（幂律α）、假设检验（GMV占比实证）、变量分解（AOV与留存率）及敏感性分析（退出概率与阈值），逻辑上层层递进且覆盖父节点的核心计算与验证环节，无重复或矛盾。）
