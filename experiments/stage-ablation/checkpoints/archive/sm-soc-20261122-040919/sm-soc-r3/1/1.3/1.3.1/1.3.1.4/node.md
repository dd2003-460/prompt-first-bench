# N154: 买家信任度下降系数 d 与 FPR 的函数关系：d = β * FPR^γ。基于 N118 的回归结果，若 β=0.4, γ=1.0，则 d=0.4 * FPR

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: stochastic
- **rework_count**: 0
- **parent_ids**: N38

## Claim

买家信任度下降系数 d 与 FPR 的函数关系：d = β * FPR^γ。基于 N118 的回归结果，若 β=0.4, γ=1.0，则 d=0.4 * FPR。当 FPR 从 0.1 升至 0.3 时，d 从 0.04 升至 0.12。此线性关系假设需通过平台 A/B 测试数据验证，若实际数据呈现非线性（如 γ>1），则高 FPR 下信任度下降更快，均衡更不稳定。

## Corrected Claim

买家信任度下降系数 d 与 FPR 的函数关系：d = β * FPR^γ。基于 N118 的回归结果，若 β=0.4, γ=1.0，则 d=0.4 * FPR。当 FPR 从 0.1 升至 0.3 时，d 从 0.04 升至 0.12。此线性关系假设需通过平台 A/B 测试数据验证，若实际数据呈现非线性（如 γ>1），则高 FPR 下信任度下降更快，均衡更不稳定。

## Evidence

先验知识/题面给定，逻辑校验通过：公式 d=0.4*FPR 在 FPR=0.1 时 d=0.04，FPR=0.3 时 d=0.12，数值计算准确，线性关系假设及非线性风险讨论逻辑自洽。

## Search Query

buyer trust decline function of false positive rate nonlinear
