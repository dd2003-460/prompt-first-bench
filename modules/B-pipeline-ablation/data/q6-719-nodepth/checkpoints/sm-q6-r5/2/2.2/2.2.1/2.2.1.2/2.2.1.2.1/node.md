# N513: 短视频平台热门视频 24h 重复率 P_repeat_hot 的机制分解：P_repeat_hot = P_share * P_view_after_share

- **status**: degraded
- **level**: L5
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 1
- **parent_ids**: N165

## Claim

短视频平台热门视频 24h 重复率 P_repeat_hot 的机制分解：P_repeat_hot = P_share * P_view_after_share + P_direct_revisit，其中 P_share ≈ 15-20%（社交分享率），P_view_after_share ≈ 40-60%（被分享者观看率），P_direct_revisit ≈ 10-15%（用户主动重看）。加权计算得 P_repeat_hot ≈ 0.175*0.5 + 0.125 ≈ 21.25%，与 N165 中 25% 基准值偏差在误差范围内，需校准分享率参数。

## Corrected Claim

短视频平台热门视频24h重复率可分解为分享后观看与直接重看两部分，具体数值需依据实际平台数据校准，当前估算值约21.25%。

## Evidence

[质询]该陈述将具体的经验参数（如分享率15-20%、重看率10-15%）作为既定事实进行计算，但这些数值属于特定平台或特定时期的经验统计数据，并非第一性原理可推导的数学或物理常数，且缺乏来源支持其具体量级。 | 经验事实，逻辑自洽但缺来源支持

## Search Query

short video platform user repeat view rate social sharing behavior statistics
