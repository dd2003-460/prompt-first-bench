# N47: T_LRU 的计算公式：T_LRU = C / (Σ_{i=1}^{k_eff} λ_i * S_i)，其中 k_eff 是满足 Σ_{i=1}^{k_eff}

- **status**: pending
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N16, N17, N18

## Claim

T_LRU 的计算公式：T_LRU = C / (Σ_{i=1}^{k_eff} λ_i * S_i)，其中 k_eff 是满足 Σ_{i=1}^{k_eff} S_i <= C 的最大对象数，λ_i 是对象 i 的请求速率（次/天），S_i 是对象 i 的大小（bytes）。

## Corrected Claim

T_LRU 的计算公式：T_LRU = C / (Σ_{i=1}^{k_eff} λ_i * S_i)，其中 k_eff 是满足 Σ_{i=1}^{k_eff} S_i <= C 的最大对象数，λ_i 是对象 i 的请求速率（次/天），S_i 是对象 i 的大小（bytes）。

## Evidence

父节点级核验未通过：不完备, 有冗余（1. 完备性不足：父节点是通用计算公式，子节点仅提供了两个特定场景（头部/长尾）的数值实例，未覆盖公式中各变量（C, λ, S）的通用定义、单位约束或边界条件（如 k_eff 的确定逻辑），导致从子节点无法还原父节点的完整理论框架。2. 冗余度高：两个子节点本质上是同一公式在不同参数集（不同的 λ 和 S 分布）下的具体计算案例，属于‘一个公式的多个取值’，而非独立的概念分支。）
