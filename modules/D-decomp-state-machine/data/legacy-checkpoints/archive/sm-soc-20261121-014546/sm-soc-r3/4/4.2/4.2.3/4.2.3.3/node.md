# N293: 建议可信度 C_cred：买家和卖家对平台推荐价准确性的信任指标，定义为平台历史推荐价与实际成交价的平均绝对百分比误差 MAPE 的倒数，C_cred = 1 

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N87

## Claim

建议可信度 C_cred：买家和卖家对平台推荐价准确性的信任指标，定义为平台历史推荐价与实际成交价的平均绝对百分比误差 MAPE 的倒数，C_cred = 1 / MAPE，若 MAPE = 10%，则 C_cred = 10。

## Corrected Claim

建议可信度 C_cred：买家和卖家对平台推荐价准确性的信任指标，定义为平台历史推荐价与实际成交价的平均绝对百分比误差 MAPE 的倒数，C_cred = 1 / MAPE，若 MAPE = 10%，则 C_cred = 10。

## Evidence

先验知识/题面给定，逻辑校验通过：MAPE定义为平均绝对百分比误差，其倒数在数学上直接对应可信度指标，数值示例（1/0.1=10）计算正确，无内部矛盾。
