# N28: 时间贴现率 α = 0.01/day 的校准依据：基于二手平台卖家行为数据，当 T_deal 从 10天 增加到 20天 时，卖家接受价格的下调幅度 ΔP/P 

- **status**: pending
- **level**: L3
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N7

## Claim

时间贴现率 α = 0.01/day 的校准依据：基于二手平台卖家行为数据，当 T_deal 从 10天 增加到 20天 时，卖家接受价格的下调幅度 ΔP/P ≈ 10%，符合 exp(-0.01*10) ≈ 0.905 的效用衰减，该参数在季节性波动期间（如节假日）可能上升至 α = 0.02/day。

## Corrected Claim

时间贴现率 α 的校准通常基于卖家行为数据，例如当交易周期 T_deal 从 10天 增加到 20天 时，卖家接受价格的下调幅度 ΔP/P 约为 10%，这符合 exp(-0.01*10) ≈ 0.905 的效用衰减模型；在季节性波动期间（如节假日），该参数可能上升至 α = 0.02/day。

## Evidence

父节点级核验未通过：不完备（子节点1关注参数构成的结构性分解（异质性来源），子节点2关注参数随时间变化的动态触发条件，两者在逻辑维度上正交且无冗余。然而，父节点中明确提到的核心‘校准依据’（即基于二手平台卖家行为数据，T_deal从10天增至20天对应10%价格下调的经验验证过程）未被任何子节点覆盖，导致分解不完备。）

## Search Query

seller time discount rate calibration second-hand platform deal duration price adjustment empirical data
