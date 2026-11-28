# N204: Agent 循环累积等待时间惩罚系数：假设科研循环平均 10 步，每步调用 1 次 LLM；若本地平均延迟 T_local=5s，云端平均延迟 T_cloud=

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N71

## Claim

Agent 循环累积等待时间惩罚系数：假设科研循环平均 10 步，每步调用 1 次 LLM；若本地平均延迟 T_local=5s，云端平均延迟 T_cloud=8s (含排队)，则总时间差 ΔT_total = 10 * (8-5) = 30s/循环；若任务需 100 个循环，差异累积为 50 分钟，显著影响迭代速度。

## Corrected Claim

Agent 循环累积等待时间惩罚系数：假设科研循环平均 10 步，每步调用 1 次 LLM；若本地平均延迟 T_local=5s，云端平均延迟 T_cloud=8s (含排队)，则总时间差 ΔT_total = 10 * (8-5) = 30s/循环；若任务需 100 个循环，差异累积为 50 分钟，显著影响迭代速度。

## Evidence

先验知识/题面给定，逻辑校验通过：算术计算正确（10步*3秒/步=30秒/循环，100循环*30秒=3000秒=50分钟），量纲与量级合理。
