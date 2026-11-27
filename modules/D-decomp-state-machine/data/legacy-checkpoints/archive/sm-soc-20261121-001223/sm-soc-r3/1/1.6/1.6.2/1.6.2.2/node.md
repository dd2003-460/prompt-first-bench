# N132: 观察窗口 T_observation 的标准化定义：将 T_observation 固定为平台平均成交周期的 75 分位数（P75），以消除长尾效应；若 P75

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N48

## Claim

观察窗口 T_observation 的标准化定义：将 T_observation 固定为平台平均成交周期的 75 分位数（P75），以消除长尾效应；若 P75 无法获取，则使用 30 天作为标准基准窗口，确保 P(Short Cycle | Baseline) 的计算具有可比性。

## Corrected Claim

观察窗口 T_observation 的标准化定义：将 T_observation 固定为平台平均成交周期的 75 分位数（P75），以消除长尾效应；若 P75 无法获取，则使用 30 天作为标准基准窗口，确保 P(Short Cycle | Baseline) 的计算具有可比性。

## Evidence

先验知识/题面给定，逻辑校验通过

## Search Query

standard observation window for transaction cycle analysis e-commerce
