# N15: LRU有效命中率折扣因子 D_eff = H_effective / H_static，其中 H_effective = H_static * (1 - M_i

- **status**: verified
- **level**: L2
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N3

## Claim

LRU有效命中率折扣因子 D_eff = H_effective / H_static，其中 H_effective = H_static * (1 - M_invalidation)，H_static 为无更新情况下的稳态命中率，D_eff 直接反映更新率对命中率的线性折扣效应。

## Corrected Claim

LRU有效命中率折扣因子 D_eff = H_effective / H_static，其中 H_effective = H_static * (1 - M_invalidation)，H_static 为无更新情况下的稳态命中率，D_eff 直接反映更新率对命中率的线性折扣效应。

## Evidence

父节点级核验通过：正交+完备+无冗余（三个子节点分别覆盖了折扣因子的简化计算（代数化简）、数值敏感性分析（依赖H_static）以及模型近似的适用边界（线性vs指数），三者维度不同，互不重叠且共同构成了对父节点公式的完整解读。）
