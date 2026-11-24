# N338: 热点内容工作集大小 W_active (GB) 基于Zipf分布计算：W_active = Q_day * s_weighted * (1 - P_tail)，

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N105

## Claim

热点内容工作集大小 W_active (GB) 基于Zipf分布计算：W_active = Q_day * s_weighted * (1 - P_tail)，其中 P_tail 为长尾请求占比（典型 10-20%），Q_day ≈ 2,048,000，s_weighted ≈ 1.5-5MB（混合图片/视频），故 W_active 范围需根据实际业务分布确定。

## Corrected Claim

热点内容工作集大小 W_active (GB) 基于Zipf分布计算：W_active = Q_day * s_weighted * (1 - P_tail)，其中 P_tail 为长尾请求占比（典型 10-20%），Q_day ≈ 2,048,000，s_weighted ≈ 1.5-5MB（混合图片/视频），故 W_active 范围需根据实际业务分布确定。

## Evidence

先验知识/题面给定，逻辑校验通过
