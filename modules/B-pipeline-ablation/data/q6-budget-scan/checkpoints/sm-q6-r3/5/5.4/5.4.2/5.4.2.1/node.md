# N322: K_peak=1.5工作点（中等波动）：月成本 Cost_monthly = Base_Cost × 1.5 × (1+0.15) = Base_Cost × 

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N103

## Claim

K_peak=1.5工作点（中等波动）：月成本 Cost_monthly = Base_Cost × 1.5 × (1+0.15) = Base_Cost × 1.725，即单位成本增加72.5%；对应日均2TB流量，峰值带宽≈3.3Gbps（2TB/日÷86400s×8×1.5），若按峰值计费需采购4Gbps带宽，月租约¥35000-50000（一线城市），单位成本C_unit_peak = ¥40000/(2×30×1.5) ≈ ¥4.4/GB。

## Corrected Claim

K_peak=1.5工作点（中等波动）：月成本 Cost_monthly = Base_Cost × 1.5 × (1+0.15) = Base_Cost × 1.725，即单位成本增加72.5%；对应日均2TB流量，峰值带宽≈3.3Gbps（2TB/日÷86400s×8×1.5），若按峰值计费需采购4Gbps带宽，月租约¥35000-50000（一线城市），单位成本C_unit_peak = ¥40000/(2×30×1.5) ≈ ¥4.4/GB。

## Evidence

先验知识/题面给定，逻辑校验通过：数学计算（1.5*1.15=1.725, 2TB/86400*8*1.5≈3.33Gbps, 40000/90≈4.44）均准确，量级符合一线城市带宽市场常识。
