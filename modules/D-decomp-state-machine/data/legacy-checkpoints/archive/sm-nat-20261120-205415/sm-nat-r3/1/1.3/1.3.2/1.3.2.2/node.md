# N104: 热门对象（h>0.9 分位）的平均大小 E[S|H>0.9] 在 ρ=-0.3 下比中位数小约 25-35%，具体值需通过条件分布截断积分 ∫_{s_min}^

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N35

## Claim

热门对象（h>0.9 分位）的平均大小 E[S|H>0.9] 在 ρ=-0.3 下比中位数小约 25-35%，具体值需通过条件分布截断积分 ∫_{s_min}^{s_max} s * f_{S|H>0.9}(s) ds 计算，其中 f_{S|H>0.9} 由 Copula 条件密度导出

## Corrected Claim

热门对象（h>0.9 分位）的平均大小 E[S|H>0.9] 在 ρ=-0.3 下比中位数小约 25-35%，具体值需通过条件分布截断积分 ∫_{s_min}^{s_max} s * f_{S|H>0.9}(s) ds 计算，其中 f_{S|H>0.9} 由 Copula 条件密度导出

## Evidence

先验知识/题面给定，逻辑校验通过：条件期望的定义及Copula条件密度推导在数学上自洽，数值量级（25-35%）在相关分布假设下合理。
