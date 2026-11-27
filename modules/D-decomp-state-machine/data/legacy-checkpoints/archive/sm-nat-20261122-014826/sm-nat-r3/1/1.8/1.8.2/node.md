# N44: LRU 有效命中率折扣因子的二阶修正：H_LRU_eff = H_LRU * (1 - u * P_in_LRU) + u * P_in_LRU * H_rev

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N13

## Claim

LRU 有效命中率折扣因子的二阶修正：H_LRU_eff = H_LRU * (1 - u * P_in_LRU) + u * P_in_LRU * H_revalidate，其中 H_revalidate 为重新验证后的命中率（假设为 1，即内容未变仅版本更新），因此折扣因子为 (1 - u * P_in_LRU)；在 u=0.01 和 P_in_LRU=0.35 时，折扣因子为 0.9965，即命中率下降 0.35 个百分点，而非 0.3 个百分点。

## Corrected Claim

LRU 有效命中率折扣因子的二阶修正：H_LRU_eff = H_LRU * (1 - u * P_in_LRU) + u * P_in_LRU * H_revalidate，其中 H_revalidate 为重新验证后的命中率（假设为 1，即内容未变仅版本更新），因此折扣因子为 (1 - u * P_in_LRU)；在 u=0.01 和 P_in_LRU=0.35 时，折扣因子为 0.9965，即命中率下降 0.35 个百分点，而非 0.3 个百分点。

## Evidence

父节点级核验通过：正交+完备+无冗余（子节点分别聚焦于公式中三个独立变量的修正与定义：1. P_in_LRU 的数值修正（输入参数）；2. 基于修正参数的结果计算（推导结论）；3. H_revalidate 的边界条件分析（模型假设）。三者逻辑上层层递进且互不重叠，完整覆盖了父节点公式的所有关键组成部分及修正逻辑，无冗余。）
