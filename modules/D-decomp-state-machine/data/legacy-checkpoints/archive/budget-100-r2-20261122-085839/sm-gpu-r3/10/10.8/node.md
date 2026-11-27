# N117: TCO 对比中电力成本的量化影响：在 24/7 运行场景下，电力成本 = TDP_Watts * 24 * 365 * Electricity_Rate_per

- **status**: pending
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N31

## Claim

TCO 对比中电力成本的量化影响：在 24/7 运行场景下，电力成本 = TDP_Watts * 24 * 365 * Electricity_Rate_per_kWh，需分别计算 2× RTX 3090 (2x350W)、1× A6000 Ada (300W)、1× H100 (700W) 的年度电力成本，并评估其对总 TCO 的占比（假设 Electricity_Rate=0.15/kWh），判断在高预算方案中电力成本是否显著影响性价比排序。

## Corrected Claim

TCO 对比中电力成本的量化影响：在 24/7 运行场景下，电力成本 = TDP_Watts * 24 * 365 * Electricity_Rate_per_kWh，需分别计算 2× RTX 3090 (2x350W)、1× A6000 Ada (300W)、1× H100 (700W) 的年度电力成本，并评估其对总 TCO 的占比（假设 Electricity_Rate=0.15/kWh），判断在高预算方案中电力成本是否显著影响性价比排序。

## Evidence

父节点级核验未通过：有冗余（子节点1、2、3本质上是同一计算公式（电力成本及其占比）在不同硬件参数下的具体实例化，存在高度结构性冗余；父节点要求的‘判断是否显著影响排序’仅由子节点4部分覆盖，且子节点4中关于RTX 3090的定性结论（敏感区间）与子节点1中计算出的占比（108%）在逻辑层级上割裂，未形成统一的决策闭环。）
