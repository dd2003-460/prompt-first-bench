# N165: P_repeat 的量化模型：用户 24h 内重复请求同一对象的概率。对于短视频平台，基于社交分享行为，热门视频 24h 重复率 P_repeat ≈ 20%-

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N53

## Claim

P_repeat 的量化模型：用户 24h 内重复请求同一对象的概率。对于短视频平台，基于社交分享行为，热门视频 24h 重复率 P_repeat ≈ 20%-30%；对于非热门长尾视频，P_repeat ≈ 5%-10%。加权平均（假设 80% 流量来自热门，20% 来自长尾），P_repeat_avg = 0.8*25% + 0.2*8% = 21.6%。

## Corrected Claim

P_repeat 的量化模型：用户 24h 内重复请求同一对象的概率。对于短视频平台，基于社交分享行为，热门视频 24h 重复率 P_repeat ≈ 20%-30%；对于非热门长尾视频，P_repeat ≈ 5%-10%。加权平均（假设 80% 流量来自热门，20% 来自长尾），P_repeat_avg = 0.8*25% + 0.2*8% = 21.6%。

## Evidence

先验知识/题面给定，逻辑校验通过
