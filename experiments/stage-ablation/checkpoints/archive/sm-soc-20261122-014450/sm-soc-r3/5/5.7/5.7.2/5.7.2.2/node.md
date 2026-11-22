# N337: Shapley 值 φ_i 的计算需遍历所有变量子集 S ⊆ {1..d}\{i}，公式为 φ_i = Σ_{S} [ (|S|!(d-|S|-1)! / d!

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N107

## Claim

Shapley 值 φ_i 的计算需遍历所有变量子集 S ⊆ {1..d}\{i}，公式为 φ_i = Σ_{S} [ (|S|!(d-|S|-1)! / d!) * (f(S ∪ {i}) - f(S)) ]，其中 f(S) 为仅使用变量集合 S 时的预测方差，该组合爆炸问题在 d=5 时可行，但需预设 f(S) 的近似估计方法（如多项式混沌展开）以控制计算成本。

## Corrected Claim

Shapley 值 φ_i 的计算需遍历所有变量子集 S ⊆ {1..d}\{i}，公式为 φ_i = Σ_{S} [ (|S|!(d-|S|-1)! / d!) * (f(S ∪ {i}) - f(S)) ]，其中 f(S) 为仅使用变量集合 S 时的预测方差，该组合爆炸问题在 d=5 时可行，但需预设 f(S) 的近似估计方法（如多项式混沌展开）以控制计算成本。

## Evidence

先验知识/题面给定，逻辑校验通过：Shapley值公式及组合爆炸特性符合数学定义，d=5时子集数量2^4=16，计算完全可行，逻辑自洽。

## Search Query

Shapley value calculation combinatorial explosion approximation polynomial chaos expansion
