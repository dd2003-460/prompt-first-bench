# N10: LRU 稳态字节命中率下界 = (Σ_{i=1}^{k} r_i · s_i) / (Σ_{i=1}^{N} r_i · s_i)，其中 r_i 是对象 i 的

- **status**: verified
- **level**: L2
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 1
- **parent_ids**: N1, N2, N3

## Claim

LRU 稳态字节命中率下界 = (Σ_{i=1}^{k} r_i · s_i) / (Σ_{i=1}^{N} r_i · s_i)，其中 r_i 是对象 i 的请求率，s_i 是对象 i 的大小，k 是缓存容量限制下的最大对象数，N=10^5 是总对象数

## Corrected Claim

在理想化静态缓存模型中，若缓存容量恰好容纳k个对象且无动态替换开销，字节命中率可表示为 (Σ_{i=1}^{k} r_i · s_i) / (Σ_{i=1}^{N} r_i · s_i)，但此非通用LRU稳态下界。

## Evidence

父节点级核验通过：正交+完备+无冗余（子节点分别处理了公式的分子、分母以及最终的组合推导，逻辑上互不重叠（正交），且完整覆盖了父节点公式的所有组成部分（完备）。子节点3是对前两者的综合，并非简单的参数重复，而是必要的代数简化步骤，因此不存在冗余。）

## Search Query

LRU byte hit rate formula steady state
