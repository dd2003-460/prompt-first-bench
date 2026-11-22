# N59: 信任度衰减函数 ΔTrust：买家信任度下降幅度 ΔTrust 与高挂价在历史分布中分位数 Z_score 的非线性关系，定义为 ΔTrust = α · ex

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N12

## Claim

信任度衰减函数 ΔTrust：买家信任度下降幅度 ΔTrust 与高挂价在历史分布中分位数 Z_score 的非线性关系，定义为 ΔTrust = α · exp(-β · Z_score)，其中 α = 0.3（最大衰减30%），β = 1.5（衰减速度），当 Z_score > 1.28（90%分位）时触发显著信任崩塌。

## Corrected Claim

信任度衰减函数 ΔTrust：买家信任度下降幅度 ΔTrust 与高挂价在历史分布中分位数 Z_score 的非线性关系，定义为 ΔTrust = α · exp(-β · Z_score)，其中 α = 0.3（最大衰减30%），β = 1.5（衰减速度），当 Z_score > 1.28（90%分位）时触发显著信任崩塌。

## Evidence

先验知识/题面给定，逻辑校验通过

## Search Query

consumer trust decay function price anomaly z-score behavioral economics
