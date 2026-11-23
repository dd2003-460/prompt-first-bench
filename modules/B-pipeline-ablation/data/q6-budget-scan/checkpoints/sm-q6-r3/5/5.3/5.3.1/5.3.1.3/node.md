# N246: Top-K 对象选择的热度稳定性窗口 T_stability：预热对象列表需基于过去 T_stability 时间窗口的热度数据生成，若对象热度半衰期 t_ha

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N78

## Claim

Top-K 对象选择的热度稳定性窗口 T_stability：预热对象列表需基于过去 T_stability 时间窗口的热度数据生成，若对象热度半衰期 t_half < T_stability，则预热列表过期率 p_stale = 1 - e^(-T_stability/t_half) 导致预热无效对象占比增加，建议 T_stability ≈ t_half（图片/视频热点半衰期通常为 1-6 小时）

## Corrected Claim

Top-K 对象选择的热度稳定性窗口 T_stability：预热对象列表需基于过去 T_stability 时间窗口的热度数据生成，若对象热度半衰期 t_half < T_stability，则预热列表过期率 p_stale = 1 - e^(-T_stability/t_half) 导致预热无效对象占比增加，建议 T_stability ≈ t_half（图片/视频热点半衰期通常为 1-6 小时）

## Evidence

先验知识/题面给定，逻辑校验通过：指数衰减模型下，时间窗口等于半衰期时过期率约为63%，符合数学推导；图片/视频热点半衰期1-6小时符合互联网内容传播的经验规律。
