# N384: 失败重试的指数退避策略对总延迟的影响：假设重试策略为指数退避（初始 1s，最大 60s，最多 5 次）。若首次失败，平均重试延迟 E[T_retry] ≈ 1 

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N130

## Claim

失败重试的指数退避策略对总延迟的影响：假设重试策略为指数退避（初始 1s，最大 60s，最多 5 次）。若首次失败，平均重试延迟 E[T_retry] ≈ 1 + 2 + 4 + 8 + 16 = 31s。若 P_fail = 63%，则平均总延迟增加 E[Extra_Delay] = P_fail * E[T_retry] ≈ 0.63 * 31s ≈ 19.5s。

## Corrected Claim

失败重试的指数退避策略对总延迟的影响：假设重试策略为指数退避（初始 1s，最大 60s，最多 5 次）。若首次失败，平均重试延迟 E[T_retry] ≈ 1 + 2 + 4 + 8 + 16 = 31s。若 P_fail = 63%，则平均总延迟增加 E[Extra_Delay] = P_fail * E[T_retry] ≈ 0.63 * 31s ≈ 19.5s。

## Evidence

先验知识/题面给定，逻辑校验通过：指数退避序列求和及期望延迟计算符合数学定义与概率论基本法则。
