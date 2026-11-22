# N198: N69 中 H_eff 的线性叠加公式 H_eff = 0.5 * H_static + 0.5 * H_update 缺乏物理基础，正确的有效命中率应为字节加

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N69

## Claim

N69 中 H_eff 的线性叠加公式 H_eff = 0.5 * H_static + 0.5 * H_update 缺乏物理基础，正确的有效命中率应为字节加权期望值 H_eff = Σ p_i s_i * [1 - P_invalid(i)] / Σ p_i s_i，在 W_LRU ≈ T_update 时，需重新计算各对象的 P_invalid(i) 并加权，而非简单取平均。

## Corrected Claim

N69 中 H_eff 的线性叠加公式 H_eff = 0.5 * H_static + 0.5 * H_update 缺乏物理基础，正确的有效命中率应为字节加权期望值 H_eff = Σ p_i s_i * [1 - P_invalid(i)] / Σ p_i s_i，在 W_LRU ≈ T_update 时，需重新计算各对象的 P_invalid(i) 并加权，而非简单取平均。

## Evidence

先验知识/题面给定，逻辑校验通过：简单算术平均忽略了不同对象访问频率（p_i）和大小（s_i）的差异，不符合加权期望值的定义；在缓存失效概率随时间变化的场景下，字节加权期望值确实是更严谨的有效命中率定义。
