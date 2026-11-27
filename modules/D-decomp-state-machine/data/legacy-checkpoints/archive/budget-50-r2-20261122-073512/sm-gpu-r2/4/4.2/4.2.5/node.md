# N152: PUE（电能利用效率）对 OPEX 的修正项：实际电力消耗 = P_tco_total × PUE；消费级本地工作站 PUE ≈ 1.0（无数据中心级冷却开销）

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N24

## Claim

PUE（电能利用效率）对 OPEX 的修正项：实际电力消耗 = P_tco_total × PUE；消费级本地工作站 PUE ≈ 1.0（无数据中心级冷却开销）；数据中心 PUE ≈ 1.2-1.4（典型范围）；需将 PUE 乘入 OPEX_power 计算：OPEX_power_corrected = P_tco_total × T_hours × E_unit_price × PUE。

## Corrected Claim

PUE（电能利用效率）对 OPEX 的修正项：实际电力消耗 = P_tco_total × PUE；消费级本地工作站 PUE ≈ 1.0（无数据中心级冷却开销）；数据中心 PUE ≈ 1.2-1.4（典型范围）；需将 PUE 乘入 OPEX_power 计算：OPEX_power_corrected = P_tco_total × T_hours × E_unit_price × PUE。

## Evidence

先验知识/题面给定，逻辑校验通过：PUE定义即为总能耗/IT能耗，故总电耗=IT功耗×PUE；消费级无额外冷却PUE≈1.0，数据中心典型PUE 1.2-1.4符合行业常识，公式推导自洽。

## Search Query

PUE power usage effectiveness data center typical range 1.2 1.4
