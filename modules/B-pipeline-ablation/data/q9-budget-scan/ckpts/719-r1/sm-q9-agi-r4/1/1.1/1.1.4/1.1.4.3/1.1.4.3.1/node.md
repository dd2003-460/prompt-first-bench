# N375: Baseline_PassRate 的计算方法：取 Qwen3.8-27B 在目标基准 (SWE-bench Medium + LiveCodeBench Sc

- **status**: verified
- **level**: L5
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N120

## Claim

Baseline_PassRate 的计算方法：取 Qwen3.8-27B 在目标基准 (SWE-bench Medium + LiveCodeBench Sci) 上最近 3 次评估的平均 Pass@1 值，若三次结果为 34%, 36%, 35%，则 Baseline_PassRate = 35%

## Corrected Claim

Baseline_PassRate 的计算方法：取 Qwen3.8-27B 在目标基准 (SWE-bench Medium + LiveCodeBench Sci) 上最近 3 次评估的平均 Pass@1 值，若三次结果为 34%, 36%, 35%，则 Baseline_PassRate = 35%

## Evidence

先验知识/题面给定，逻辑校验通过：算术平均计算正确 ((34+36+35)/3=35)，定义清晰且无内部矛盾。
