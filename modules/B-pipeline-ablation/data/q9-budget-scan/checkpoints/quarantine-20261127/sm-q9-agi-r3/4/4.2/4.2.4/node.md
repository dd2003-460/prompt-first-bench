# N68: T_acc 阈值设定为 0.85（对应 N25 的可发表级综合得分下限）；当 local_27b 的 Self-Consistency 采样（k=5）一致率低于

- **status**: verified
- **level**: L3
- **source**: given
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N22

## Claim

T_acc 阈值设定为 0.85（对应 N25 的可发表级综合得分下限）；当 local_27b 的 Self-Consistency 采样（k=5）一致率低于 0.85 时，判定为低置信度任务，强制进入 cloud_api 或 human_review 分支。

## Corrected Claim

T_acc 阈值设定为 0.85（对应 N25 的可发表级综合得分下限）；当 local_27b 的 Self-Consistency 采样（k=5）一致率低于 0.85 时，判定为低置信度任务，强制进入 cloud_api 或 human_review 分支。

## Evidence

先验知识/题面给定，逻辑校验通过
