# N16: 有效命中率折损因子：H_eff = H_lru * (1 - P_inval * (1 - H_lru))，当 P_inval < 0.1 时，折损约 10%-

- **status**: verified
- **level**: L2
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N4

## Claim

有效命中率折损因子：H_eff = H_lru * (1 - P_inval * (1 - H_lru))，当 P_inval < 0.1 时，折损约 10%-20%；当 P_inval > 0.5 时，折损超过 50%。

## Corrected Claim

有效命中率折损因子：H_eff = H_lru * (1 - P_inval * (1 - H_lru))，当 P_inval < 0.1 时，折损约 10%-20%；当 P_inval > 0.5 时，折损超过 50%。

## Evidence

父节点级核验通过：正交+完备+无冗余（子节点逻辑清晰且正交：节点1聚焦于 P_inval 的数值推导与物理意义（极低概率）；节点2聚焦于更新对热点基线 H_lru 本身的潜在侵蚀（间接影响/一致性成本）；节点3基于节点1的结果进行最终公式量化，得出直接命中率折损微乎其微的结论。三者分别对应‘参数值’、‘副作用/基线漂移’、‘最终结果’，无重复且无矛盾。）

## Search Query

cache hit rate decay due to object updates
