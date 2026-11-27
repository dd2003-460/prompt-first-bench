# N243: 算法噪声的'系统性偏差'修正：σ_algo 并非纯随机，而是与商品属性（如价格偏离度 D）相关，高偏离度商品可能被算法降权（惩罚项 W_penalty = -γ

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: stochastic
- **rework_count**: 0
- **parent_ids**: N66

## Claim

算法噪声的'系统性偏差'修正：σ_algo 并非纯随机，而是与商品属性（如价格偏离度 D）相关，高偏离度商品可能被算法降权（惩罚项 W_penalty = -γ * D），导致 σ_algo_effective = σ_algo_base * (1 + γ * |D|)；假设 γ = 0.2，则 D=20% 时有效噪声放大 4%，需从总方差中分离出系统性部分。

## Corrected Claim

算法噪声的'系统性偏差'修正：σ_algo 并非纯随机，而是与商品属性（如价格偏离度 D）相关，高偏离度商品可能被算法降权（惩罚项 W_penalty = -γ * D），导致 σ_algo_effective = σ_algo_base * (1 + γ * |D|)；假设 γ = 0.2，则 D=20% 时有效噪声放大 4%，需从总方差中分离出系统性部分。

## Evidence

先验知识/题面给定，逻辑校验通过：数学推导正确（1+0.2*0.2=1.04，即放大4%），概念定义自洽，无外部来源矛盾。
