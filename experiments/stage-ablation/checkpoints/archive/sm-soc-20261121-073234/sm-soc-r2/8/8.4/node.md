# N114: 阈值敏感性分析：若 Threshold_stop 设定为 20%，则只有当挂价低于保留价 20% 时买家才行动；结合 N6 的 15-25% 溢价，这意味着买家

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N33

## Claim

阈值敏感性分析：若 Threshold_stop 设定为 20%，则只有当挂价低于保留价 20% 时买家才行动；结合 N6 的 15-25% 溢价，这意味着买家需要看到价格从溢价 25% 降至低于保留价 20%（即总降幅需超过 45%）才会咨询，解释了为何常规小幅降价无效。

## Corrected Claim

阈值敏感性分析：若 Threshold_stop 设定为 20%，则只有当挂价低于保留价 20% 时买家才行动；结合 N6 的 15-25% 溢价，这意味着买家需要看到价格从溢价 25% 降至低于保留价 20%（即总降幅需超过 45%）才会咨询，解释了为何常规小幅降价无效。

## Evidence

先验知识/题面给定，逻辑校验通过：从溢价25%降至低于保留价20%的数学推导正确（1.25 * (1-0.45) = 0.6875 < 0.8），且符合阈值敏感性分析的基本逻辑。

## Search Query

price discount threshold buyer response rate second hand marketplace
