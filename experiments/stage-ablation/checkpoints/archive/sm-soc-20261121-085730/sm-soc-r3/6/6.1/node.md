# N129: 稀缺性启发式的心理阈值（P > 1.15 * C_ref）并非固定常数，而是随商品类别的标准化程度S标准化（S∈[0,1]）动态变化，阈值系数k_scarcit

- **status**: verified
- **level**: L3
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N39

## Claim

稀缺性启发式的心理阈值（P > 1.15 * C_ref）并非固定常数，而是随商品类别的标准化程度S标准化（S∈[0,1]）动态变化，阈值系数k_scarcity = 1.15 - 0.2*S（标准化程度越高，阈值越低）。

## Corrected Claim

稀缺性启发式的心理阈值可能随商品类别的标准化程度动态变化，但具体阈值系数k_scarcity = 1.15 - 0.2*S的线性关系缺乏直接证据支持，需进一步实证研究验证。

## Evidence

父节点级核验通过：正交+完备+无冗余（子节点分别对应父节点中核心变量S的操作化定义、模型边界条件（失效情形）以及参数校准方法，三者维度独立（定义 vs 边界 vs 验证），无重复或矛盾，且完整覆盖了父节点公式中涉及的所有关键要素（S的定义、系数的适用性、系数的实证依据）。）

## Search Query

scarcity heuristic price threshold standardization level consumer psychology

## Retrieval Sources

- {'url': 'https://quickmath.com/&rut=768cbf7c1c85d44a467a0bce9aa2b46bb1d9b926eacdc7db8750be8c61b18c96', 'type': 'ddg', 'title': 'solve form - Step-by-Step Math Problem Solver'}
