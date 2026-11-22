# N75: N21 中 0.82 的下界对应于‘请求命中率’而非‘字节命中率’：在字节命中率口径下，需计算加权项 Σ(R_i*S_i)/Σ(R_j*S_j)，由于热门对象通

- **status**: pending
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N21

## Claim

N21 中 0.82 的下界对应于‘请求命中率’而非‘字节命中率’：在字节命中率口径下，需计算加权项 Σ(R_i*S_i)/Σ(R_j*S_j)，由于热门对象通常较小（ρ<0），字节命中率下界通常低于请求命中率下界 0.82。

## Corrected Claim

N21 中 0.82 的下界对应于‘请求命中率’而非‘字节命中率’：在字节命中率口径下，需计算加权项 Σ(R_i*S_i)/Σ(R_j*S_j)，由于热门对象通常较小（ρ<0），字节命中率下界通常低于请求命中率下界 0.82。

## Evidence

父节点级核验未通过：有冗余（子节点在逻辑上是正交的（针对不同参数取值），且覆盖了从基准到极端情况的完整范围。然而，三个子节点本质上是同一数学模型（H_byte = H_req * Factor(ρ)）在 ρ=0, -0.3, -0.5 三个不同参数下的具体计算实例，属于典型的‘参数化枚举’而非结构性分解，因此存在冗余。）

## Search Query

byte hit ratio vs request hit ratio Pareto distribution
