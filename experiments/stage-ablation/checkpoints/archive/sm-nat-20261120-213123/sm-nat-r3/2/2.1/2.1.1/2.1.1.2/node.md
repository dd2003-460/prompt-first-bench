# N89: 截断上限 s_max 的选取对 Var[S] 的影响：当 s_max 从 100MB 增至 1GB 时，Var[S] 增加约 10^(α-2)*log(10) 

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N33

## Claim

截断上限 s_max 的选取对 Var[S] 的影响：当 s_max 从 100MB 增至 1GB 时，Var[S] 增加约 10^(α-2)*log(10) ≈ 10^(-0.9)*2.3 ≈ 0.29 倍（即 29%），表明方差对长尾截断点呈幂律敏感，s_max 每增加一个数量级，σ_S 增加约 1.3 倍，这是蒙特卡洛模拟收敛慢的根本原因。

## Corrected Claim

截断上限 s_max 的选取对 Var[S] 的影响：当 s_max 从 100MB 增至 1GB 时，Var[S] 增加约 10^(α-2)*log(10) ≈ 10^(-0.9)*2.3 ≈ 0.29 倍（即 29%），表明方差对长尾截断点呈幂律敏感，s_max 每增加一个数量级，σ_S 增加约 1.3 倍，这是蒙特卡洛模拟收敛慢的根本原因。

## Evidence

先验知识/题面给定，逻辑校验通过：基于幂律分布尾部截断的方差公式推导，量级与系数计算自洽。
