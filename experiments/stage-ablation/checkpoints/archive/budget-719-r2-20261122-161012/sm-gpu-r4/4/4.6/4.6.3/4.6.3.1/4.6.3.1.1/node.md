# N591: 利用率因子 (Utilization_Factor) 的精确定义与测量方法：Utilization_Factor 应定义为 ‘GPU 处于 Peak Power

- **status**: verified
- **level**: L5
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N246

## Claim

利用率因子 (Utilization_Factor) 的精确定义与测量方法：Utilization_Factor 应定义为 ‘GPU 处于 Peak Power 状态的时间占比’，而非 ‘系统通电时间占比’。在本地工作站场景下，若用户每天使用 8 小时，且其中 50% 时间 GPU 满载 (Peak)，50% 时间 Idle，则日均 Utilization = (8h/24h) * 50% = 16.7%。N113 中隐含的 15-16.5% 利用率与此定义一致，但需明确区分 ‘Duty Cycle’ (通电占比) 与 ‘Load Factor’ (满载占比)。

## Corrected Claim

利用率因子 (Utilization_Factor) 的精确定义与测量方法：Utilization_Factor 应定义为 ‘GPU 处于 Peak Power 状态的时间占比’，而非 ‘系统通电时间占比’。在本地工作站场景下，若用户每天使用 8 小时，且其中 50% 时间 GPU 满载 (Peak)，50% 时间 Idle，则日均 Utilization = (8h/24h) * 50% = 16.7%。N113 中隐含的 15-16.5% 利用率与此定义一致，但需明确区分 ‘Duty Cycle’ (通电占比) 与 ‘Load Factor’ (满载占比)。

## Evidence

先验知识/题面给定，逻辑校验通过：定义清晰区分了Duty Cycle与Load Factor，数学计算 (8/24)*0.5 ≈ 16.7% 准确无误，且与N113隐含数值一致。
