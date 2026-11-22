# N107: 数值验证的敏感性分析：当 $P_{list}$ 从1000降至100（低价值商品）时，$W(30)$ 降至0.616，而 $\psi(100)$ 若 $\Del

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N38

## Claim

数值验证的敏感性分析：当 $P_{list}$ 从1000降至100（低价值商品）时，$W(30)$ 降至0.616，而 $\psi(100)$ 若 $\Delta P$ 按比例缩小至10，则 $\psi=4.5$，此时 $W < \psi$ 依然成立但差距缩小；若 $P_{list}$ 升至10000，$W$ 增至61.6，$\psi$ 增至450，差距扩大，说明高价值商品更难打破高挂价均衡，需量化不同价格区间的均衡打破难度指数。

## Corrected Claim

数值验证的敏感性分析：当 $P_{list}$ 从1000降至100（低价值商品）时，$W(30)$ 降至0.616，而 $\psi(100)$ 若 $\Delta P$ 按比例缩小至10，则 $\psi=4.5$，此时 $W < \psi$ 依然成立但差距缩小；若 $P_{list}$ 升至10000，$W$ 增至61.6，$\psi$ 增至450，差距扩大，说明高价值商品更难打破高挂价均衡，需量化不同价格区间的均衡打破难度指数。

## Evidence

先验知识/题面给定，逻辑校验通过：数值计算符合线性比例关系（W与P_list成正比，ψ与ΔP成正比），且结论（高价值商品均衡更稳固）符合经济学直觉。

## Search Query

price level effect on seller price stickiness high value goods
