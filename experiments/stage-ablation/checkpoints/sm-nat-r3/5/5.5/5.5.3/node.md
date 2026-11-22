# N90: 混合更新工作点：假设更新率按对象热度分布加权分配（即热度越高的对象更新越频繁，更新率 λ_i ∝ r_i^β），则平均失效概率 P_invalid_mixed 

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N29

## Claim

混合更新工作点：假设更新率按对象热度分布加权分配（即热度越高的对象更新越频繁，更新率 λ_i ∝ r_i^β），则平均失效概率 P_invalid_mixed = E[1 - (1-λ_i)^{T_residence_days}]，其中 λ_i 为对象 i 的日更新率；在此工作点下，折损因子 D_mixed 介于 D_uniform 和 D_concentrated 之间，具体数值取决于 β 与 T_residence_days 的耦合效应。

## Corrected Claim

混合更新工作点：假设更新率按对象热度分布加权分配（即热度越高的对象更新越频繁，更新率 λ_i ∝ r_i^β），则平均失效概率 P_invalid_mixed = E[1 - (1-λ_i)^{T_residence_days}]，其中 λ_i 为对象 i 的日更新率；在此工作点下，折损因子 D_mixed 介于 D_uniform 和 D_concentrated 之间，具体数值取决于 β 与 T_residence_days 的耦合效应。

## Evidence

父节点级核验通过：正交+完备+无冗余（三个子节点分别对应计算流程的三个独立且必要的步骤：1. 参数化更新率（λ_i）的归一化计算；2. 单个对象失效概率（P_invalid）的推导；3. 全局折损因子（D_mixed）的聚合计算。三者逻辑层层递进，无内容重复，且共同覆盖了父节点中提到的所有关键变量（λ_i, β, T_res, P_invalid, D_mixed）及计算逻辑，无冗余。）
