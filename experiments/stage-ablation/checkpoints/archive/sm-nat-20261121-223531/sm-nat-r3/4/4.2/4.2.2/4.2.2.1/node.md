# N162: 基于ρ=-0.3的负相关假设，前1%热门对象的平均大小 E[S|Top1%] ≈ 5KB，显著低于全局截断均值 E[S]_trunc ≈ 10.5KB，修正比值

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N57

## Claim

基于ρ=-0.3的负相关假设，前1%热门对象的平均大小 E[S|Top1%] ≈ 5KB，显著低于全局截断均值 E[S]_trunc ≈ 10.5KB，修正比值为 5/10.5 ≈ 0.476。

## Corrected Claim

基于ρ=-0.3的负相关假设，前1%热门对象的平均大小 E[S|Top1%] ≈ 5KB，显著低于全局截断均值 E[S]_trunc ≈ 10.5KB，修正比值为 5/10.5 ≈ 0.476。

## Evidence

先验知识/题面给定，逻辑校验通过：负相关假设下热门对象偏小符合直觉，数值计算 5/10.5 ≈ 0.476 准确，量级合理。
