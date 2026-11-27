# N123: C_norm 对命中率的弹性系数 ε_H,C：在 C_norm << 1 的极限下，H ≈ C_norm * E[1/s]，因此 dH/dC_norm ≈ E[

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N39, N40, N41

## Claim

C_norm 对命中率的弹性系数 ε_H,C：在 C_norm << 1 的极限下，H ≈ C_norm * E[1/s]，因此 dH/dC_norm ≈ E[1/s]；需计算 E[1/s] 在 α=1.1 下的数值，以量化 C_norm 从 0.119 降至 0.012 时命中率的具体下降值，而非仅定性判断 <5%。

## Corrected Claim

C_norm 对命中率的弹性系数 ε_H,C：在 C_norm << 1 的极限下，H ≈ C_norm * E[1/s]，因此 dH/dC_norm ≈ E[1/s]；需计算 E[1/s] 在 α=1.1 下的数值，以量化 C_norm 从 0.119 降至 0.012 时命中率的具体下降值，而非仅定性判断 <5%。

## Evidence

先验知识/题面给定，逻辑校验通过：在 C_norm << 1 的线性近似下，H 与 C_norm 成正比，弹性系数确实趋近于常数 E[1/s]，推导逻辑自洽。
