# N305: 奖励积分数量 N_points 的动态调整机制：奖励积分数量并非固定10分，而是与订单金额 P_order 挂钩，公式为 N_points = floor(P_

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N85, N87, N88

## Claim

奖励积分数量 N_points 的动态调整机制：奖励积分数量并非固定10分，而是与订单金额 P_order 挂钩，公式为 N_points = floor(P_order / P_threshold)，其中 P_threshold 为每满多少元送1分（假设 P_threshold = 10元）。若订单金额为 100元，N_points = 10；若为 200元，N_points = 20。

## Corrected Claim

奖励积分数量 N_points 的动态调整机制：奖励积分数量并非固定10分，而是与订单金额 P_order 挂钩，公式为 N_points = floor(P_order / P_threshold)，其中 P_threshold 为每满多少元送1分（假设 P_threshold = 10元）。若订单金额为 100元，N_points = 10；若为 200元，N_points = 20。

## Evidence

先验知识/题面给定，逻辑校验通过
