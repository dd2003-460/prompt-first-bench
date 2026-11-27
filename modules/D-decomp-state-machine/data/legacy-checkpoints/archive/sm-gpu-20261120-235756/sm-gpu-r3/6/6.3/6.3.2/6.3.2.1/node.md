# N318: RTX 5090 在持有期第 12 个月时的残值率（Residual Value Ratio）具体数值，定义为：R_12 = P_12 / P_0，其中 P_0

- **status**: degraded
- **level**: L4
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N118

## Claim

RTX 5090 在持有期第 12 个月时的残值率（Residual Value Ratio）具体数值，定义为：R_12 = P_12 / P_0，其中 P_0 为购买价（参考 N111 溢价后价格），P_12 为第 12 个月二手市场均价；需对比 RTX 4090 同期残值率（约 55-60%）以验证 75% 的预估是否成立，若 R_12 < 70% 则需修正 TCO 模型中的折旧项。

## Corrected Claim

RTX 5090 在持有期第 12 个月时的残值率（R_12 = P_12 / P_0）需基于实际二手市场数据确定；参考 RTX 4090 同期残值率（约 55-60%）作为基准，若 R_12 显著低于 70%，则需修正 TCO 模型中的折旧项。

## Evidence

[质询]该陈述包含具体的经验性数值（RTX 4090 残值率 55-60%）和预测阈值（75%），属于硬件市场经验事实，无法从第一性原理推导，且缺乏实时市场数据支持。 | 经验事实，逻辑自洽但缺来源支持（检索无可用来源，无法验证具体残值率数值及对比基准）。

## Search Query

RTX 5090 resale value 12 months depreciation rate 2025
