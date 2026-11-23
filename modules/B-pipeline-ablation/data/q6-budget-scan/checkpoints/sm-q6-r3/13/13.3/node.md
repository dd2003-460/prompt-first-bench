# N354: 目标函数 J(strategy) 的求解算法：由于 P99(strategy) 与 C_total(strategy) 均为非凸函数，需采用网格搜索（Grid 

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N111

## Claim

目标函数 J(strategy) 的求解算法：由于 P99(strategy) 与 C_total(strategy) 均为非凸函数，需采用网格搜索（Grid Search）在 α ∈ [0,1]（混合比例）和 N_pop ∈ [0,10]（自建节点数）的二维空间上离散化求解，步长 Δα=0.05, ΔN=1，取 J 最小值对应的 (α*, N_pop*) 为最优策略

## Corrected Claim

目标函数 J(strategy) 的求解算法：由于 P99(strategy) 与 C_total(strategy) 均为非凸函数，需采用网格搜索（Grid Search）在 α ∈ [0,1]（混合比例）和 N_pop ∈ [0,10]（自建节点数）的二维空间上离散化求解，步长 Δα=0.05, ΔN=1，取 J 最小值对应的 (α*, N_pop*) 为最优策略

## Evidence

先验知识/题面给定，逻辑校验通过：非凸函数在低维离散空间使用网格搜索是标准且合理的求解策略，步长设置符合常规工程实践。
