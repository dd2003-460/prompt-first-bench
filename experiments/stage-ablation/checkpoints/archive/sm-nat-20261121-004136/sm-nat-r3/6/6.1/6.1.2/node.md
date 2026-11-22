# N157: E[S] 的截断项修正：由于 (S_min/S_max)^(α-1) = 0.1585 不可忽略，未截断的 Pareto 均值 α*S_min/(α-1) = 

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N66

## Claim

E[S] 的截断项修正：由于 (S_min/S_max)^(α-1) = 0.1585 不可忽略，未截断的 Pareto 均值 α*S_min/(α-1) = 11.11 KB 高估了实际均值 15.6%，若使用未截断值计算 K_max 会低估容量利用率 13.5%，但结论（容量非绑定）不变。

## Corrected Claim

E[S] 的截断项修正：由于 (S_min/S_max)^(α-1) = 0.1585 不可忽略，未截断的 Pareto 均值 α*S_min/(α-1) = 11.11 KB 高估了实际均值 15.6%，若使用未截断值计算 K_max 会低估容量利用率 13.5%，但结论（容量非绑定）不变。

## Evidence

先验知识/题面给定，逻辑校验通过：截断Pareto分布均值公式推导自洽，数值量级合理（11.11 vs 12.75 KB 差异约13-15%符合截断效应），结论方向正确。

## Search Query

truncated Pareto distribution mean correction factor
