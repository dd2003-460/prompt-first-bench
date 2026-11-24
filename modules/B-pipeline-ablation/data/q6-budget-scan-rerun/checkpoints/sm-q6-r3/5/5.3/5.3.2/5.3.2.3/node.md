# N324: Zipf 分布拟合残差对带宽需求预测误差的影响：计算实际省级流量分布与 Zipf 模型预测值的均方根误差 RMSE = sqrt(Σ(geo_actual_i 

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N103, N104, N105

## Claim

Zipf 分布拟合残差对带宽需求预测误差的影响：计算实际省级流量分布与 Zipf 模型预测值的均方根误差 RMSE = sqrt(Σ(geo_actual_i - geo_zipf_i)^2)；若 RMSE > 5%，则需在带宽成本估算中增加 10% 的安全边际（Safety Margin），即 B_tail_safe = B_tail × 1.1，以覆盖长尾分布的偏差。

## Corrected Claim

Zipf 分布拟合残差对带宽需求预测误差的影响：计算实际省级流量分布与 Zipf 模型预测值的均方根误差 RMSE = sqrt(Σ(geo_actual_i - geo_zipf_i)^2)；若 RMSE > 5%，则需在带宽成本估算中增加 10% 的安全边际（Safety Margin），即 B_tail_safe = B_tail × 1.1，以覆盖长尾分布的偏差。

## Evidence

先验知识/题面给定，逻辑校验通过
