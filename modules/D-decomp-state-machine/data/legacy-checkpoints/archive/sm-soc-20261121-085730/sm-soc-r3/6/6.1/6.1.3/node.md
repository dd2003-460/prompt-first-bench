# N367: k_scarcity 的实证校准方法：使用平台历史数据，对每个商品类别计算实际触发'稀缺/高质'认知偏差（通过买家咨询率异常值检测）的价格阈值 P_trigge

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N129

## Claim

k_scarcity 的实证校准方法：使用平台历史数据，对每个商品类别计算实际触发'稀缺/高质'认知偏差（通过买家咨询率异常值检测）的价格阈值 P_trigger，回归 P_trigger / C_ref = k_scarcity_actual ~ S，检验斜率是否为 -0.2 且截距是否为 1.15。

## Corrected Claim

k_scarcity 的实证校准方法：使用平台历史数据，对每个商品类别计算实际触发'稀缺/高质'认知偏差（通过买家咨询率异常值检测）的价格阈值 P_trigger，回归 P_trigger / C_ref = k_scarcity_actual ~ S，检验斜率是否为 -0.2 且截距是否为 1.15。

## Evidence

先验知识/题面给定，逻辑校验通过
