# N343: 价格分段佣金率函数：k(P) = k_base * (1 - β * I(P > P_threshold))，其中 I(·) 为指示函数，β 为高价商品折扣系数

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N110

## Claim

价格分段佣金率函数：k(P) = k_base * (1 - β * I(P > P_threshold))，其中 I(·) 为指示函数，β 为高价商品折扣系数（需验证 β 的具体数值，如 0.2 表示高价商品佣金率降低 20%），P_threshold 为触发降价的高价阈值（如 P_median * 1.15）。

## Corrected Claim

价格分段佣金率函数：k(P) = k_base * (1 - β * I(P > P_threshold))，其中 I(·) 为指示函数，β 为高价商品折扣系数（需验证 β 的具体数值，如 0.2 表示高价商品佣金率降低 20%），P_threshold 为触发降价的高价阈值（如 P_median * 1.15）。

## Evidence

先验知识/题面给定，逻辑校验通过
