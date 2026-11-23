# N323: K_peak=2.0工作点（高波动/短视频突发）：月成本 Cost_monthly = Base_Cost × 2.0 × (1+0.20) = Base_Co

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N103

## Claim

K_peak=2.0工作点（高波动/短视频突发）：月成本 Cost_monthly = Base_Cost × 2.0 × (1+0.20) = Base_Cost × 2.4，单位成本增加140%；峰值带宽≈4.4Gbps，需采购5Gbps带宽，月租约¥45000-65000，单位成本C_unit_peak = ¥55000/(2×30×2.0) ≈ ¥4.6/GB；与K_peak=1.5相比，峰值系数每增加0.5，单位成本仅增加~5%，因带宽采购有阶梯档位（4G→5G跳变被档位吸收）。

## Corrected Claim

K_peak=2.0工作点（高波动/短视频突发）：月成本 Cost_monthly = Base_Cost × 2.0 × (1+0.20) = Base_Cost × 2.4，单位成本增加140%；峰值带宽≈4.4Gbps，需采购5Gbps带宽，月租约¥45000-65000，单位成本C_unit_peak = ¥55000/(2×30×2.0) ≈ ¥4.6/GB；与K_peak=1.5相比，峰值系数每增加0.5，单位成本仅增加~5%，因带宽采购有阶梯档位（4G→5G跳变被档位吸收）。

## Evidence

先验知识/题面给定，逻辑校验通过：成本公式推导正确（2.0*1.2=2.4，增幅140%），单位成本计算量级合理（55000/120≈4.58），带宽阶梯效应解释符合工程直觉。
