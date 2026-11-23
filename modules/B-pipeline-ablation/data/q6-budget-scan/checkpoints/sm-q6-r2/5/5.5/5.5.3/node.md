# N107: 混合策略的扩容弹性成本公式：Cost_scaling_mixed = (Traffic_Growth_Rate × Traffic_TB_core × Cost

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N33

## Claim

混合策略的扩容弹性成本公式：Cost_scaling_mixed = (Traffic_Growth_Rate × Traffic_TB_core × Cost_per_TB_self_hosted) + (Traffic_Growth_Rate × Traffic_TB_tail × Cost_per_TB_cloud)；其中Traffic_TB_core为80%流量，Traffic_TB_tail为20%流量，需分别计算自建和公有云部分的增量成本。

## Corrected Claim

混合策略的扩容弹性成本公式：Cost_scaling_mixed = (Traffic_Growth_Rate × Traffic_TB_core × Cost_per_TB_self_hosted) + (Traffic_Growth_Rate × Traffic_TB_tail × Cost_per_TB_cloud)；其中Traffic_TB_core为80%流量，Traffic_TB_tail为20%流量，需分别计算自建和公有云部分的增量成本。

## Evidence

先验知识/题面给定，逻辑校验通过
