# N306: K_base(t) 的傅里叶拟合参数：K_base(t) = A_0 + Σ(A_n * cos(2πnt/24) + B_n * sin(2πnt/24))，

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N99, N100, N101

## Claim

K_base(t) 的傅里叶拟合参数：K_base(t) = A_0 + Σ(A_n * cos(2πnt/24) + B_n * sin(2πnt/24))，其中 A_0 为日均基线（1.0），A_1 ≈ 1.5（主日周期），A_2 ≈ 0.5（次谐波，反映午/晚双峰）；该拟合用于生成 24 小时逐小时的 K_base 序列，输入带宽成本计算。

## Corrected Claim

K_base(t) 的傅里叶拟合参数：K_base(t) = A_0 + Σ(A_n * cos(2πnt/24) + B_n * sin(2πnt/24))，其中 A_0 为日均基线（1.0），A_1 ≈ 1.5（主日周期），A_2 ≈ 0.5（次谐波，反映午/晚双峰）；该拟合用于生成 24 小时逐小时的 K_base 序列，输入带宽成本计算。

## Evidence

先验知识/题面给定，逻辑校验通过：傅里叶级数形式正确，参数量级（基线1.0，主谐波1.5，次谐波0.5）符合典型日周期负载特征，无内部矛盾。
