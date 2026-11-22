# N118: 卖家信任度 Trust_factor 的量化模型：Trust_factor = 1 - (1 - Historical_Accuracy)^2，其中 Histo

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N40

## Claim

卖家信任度 Trust_factor 的量化模型：Trust_factor = 1 - (1 - Historical_Accuracy)^2，其中 Historical_Accuracy 为平台历史基准价与实际成交价的平均偏差率（假设平均偏差率为 0.1，则 Trust_factor = 1 - 0.81 = 0.19），若历史偏差率降至 0.05，Trust_factor 升至 0.9025，显著影响最终 δ 值。

## Corrected Claim

卖家信任度 Trust_factor 的量化模型：Trust_factor = 1 - (1 - Historical_Accuracy)^2，其中 Historical_Accuracy 为平台历史基准价与实际成交价的平均偏差率（假设平均偏差率为 0.1，则 Trust_factor = 1 - 0.81 = 0.19），若历史偏差率降至 0.05，Trust_factor 升至 0.9025，显著影响最终 δ 值。

## Evidence

先验知识/题面给定，逻辑校验通过：公式 Trust_factor = 1 - (1 - Historical_Accuracy)^2 在 Historical_Accuracy=0.1 时计算为 1 - 0.9^2 = 0.19，在 Historical_Accuracy=0.05 时计算为 1 - 0.95^2 = 0.9025，数值推导正确且逻辑自洽。

## Search Query

seller trust factor price accuracy model e-commerce
