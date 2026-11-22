# N22: 条件性推荐逻辑：最终推荐 R 是函数 R = f(Budget_B, Latency_SLA, Quality_Sensitivity, Electricity

- **status**: verified
- **level**: L2
- **source**: given
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N4

## Claim

条件性推荐逻辑：最终推荐 R 是函数 R = f(Budget_B, Latency_SLA, Quality_Sensitivity, Electricity_Rate)。若 Budget_B < 3000 USD 且 Quality_Sensitivity=Low，推荐工作点1；若 Budget_B > 5000 USD 且 Latency_SLA < 50ms/token，推荐工作点2；若 Electricity_Rate > 0.2 USD/kWh，则 TCO 中能耗占比权重 w_elec 上升，可能反转排序。无绝对排名，必须输出条件分支表

## Corrected Claim

条件性推荐逻辑：最终推荐 R 是函数 R = f(Budget_B, Latency_SLA, Quality_Sensitivity, Electricity_Rate)。若 Budget_B < 3000 USD 且 Quality_Sensitivity=Low，推荐工作点1；若 Budget_B > 5000 USD 且 Latency_SLA < 50ms/token，推荐工作点2；若 Electricity_Rate > 0.2 USD/kWh，则 TCO 中能耗占比权重 w_elec 上升，可能反转排序。无绝对排名，必须输出条件分支表

## Evidence

先验知识/题面给定，逻辑校验通过
