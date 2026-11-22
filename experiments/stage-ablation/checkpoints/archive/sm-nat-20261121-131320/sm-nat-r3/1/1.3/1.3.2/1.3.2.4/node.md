# N82: K_ρ 的蒙特卡洛模拟估算流程：生成 100 万对 (u,v) ~ Uniform(0,1)，通过 Q_S(u) 和 Q_f(v) 映射到 (S,f)，计算 K

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N26

## Claim

K_ρ 的蒙特卡洛模拟估算流程：生成 100 万对 (u,v) ~ Uniform(0,1)，通过 Q_S(u) 和 Q_f(v) 映射到 (S,f)，计算 K_ρ = E[S|f > f_median]^{-1} * E[S]，重复 10 次取均值和 95% 置信区间，预期 K_ρ ∈ [1.05, 1.15]。

## Corrected Claim

K_ρ 的蒙特卡洛模拟估算流程：生成 100 万对 (u,v) ~ Uniform(0,1)，通过 Q_S(u) 和 Q_f(v) 映射到 (S,f)，计算 K_ρ = E[S|f > f_median]^{-1} * E[S]，重复 10 次取均值和 95% 置信区间，预期 K_ρ ∈ [1.05, 1.15]。

## Evidence

先验知识/题面给定，逻辑校验通过：蒙特卡洛方法用于估算条件期望比值在统计上有效，100万样本量足以保证精度，K_ρ 定义及预期区间符合一般统计模拟逻辑。
