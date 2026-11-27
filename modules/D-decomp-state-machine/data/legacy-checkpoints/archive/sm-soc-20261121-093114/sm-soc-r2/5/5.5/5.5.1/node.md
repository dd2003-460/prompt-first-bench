# N83: 策略强度 S_min 的量化定义：S_min = (P_dev_initial - P_dev_target) / (P_dev_initial * Elast

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N26

## Claim

策略强度 S_min 的量化定义：S_min = (P_dev_initial - P_dev_target) / (P_dev_initial * Elasticity_response)，其中 P_dev_initial 为初始挂价-成交价差（20%），P_dev_target 为目标差值（10%），Elasticity_response 为卖家对平台干预措施的价格响应弹性，需通过 A/B 测试估计。

## Corrected Claim

策略强度 S_min 的量化定义：S_min = (P_dev_initial - P_dev_target) / (P_dev_initial * Elasticity_response)，其中 P_dev_initial 为初始挂价-成交价差（20%），P_dev_target 为目标差值（10%），Elasticity_response 为卖家对平台干预措施的价格响应弹性，需通过 A/B 测试估计。

## Evidence

先验知识/题面给定，逻辑校验通过
