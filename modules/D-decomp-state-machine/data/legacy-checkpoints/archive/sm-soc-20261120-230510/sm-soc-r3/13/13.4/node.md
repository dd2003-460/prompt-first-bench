# N324: 震荡频率 T_feedback 的微观决定因素：T_feedback = T_decision_cycle + T_signal_latency，其中 T_de

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N114

## Claim

震荡频率 T_feedback 的微观决定因素：T_feedback = T_decision_cycle + T_signal_latency，其中 T_decision_cycle 为卖家重新评估价格的平均间隔（典型值 24-72 小时），T_signal_latency 为平台数据反馈至卖家界面的延迟（典型值 < 1 小时），故 T_feedback ≈ T_decision_cycle。

## Corrected Claim

震荡频率 T_feedback 的微观决定因素：T_feedback = T_decision_cycle + T_signal_latency，其中 T_decision_cycle 为卖家重新评估价格的平均间隔（典型值 24-72 小时），T_signal_latency 为平台数据反馈至卖家界面的延迟（典型值 < 1 小时），故 T_feedback ≈ T_decision_cycle。

## Evidence

先验知识/题面给定，逻辑校验通过：反馈周期由决策间隔与信号延迟串联组成，量级合理（24-72h + <1h ≈ 24-72h），符合动态定价系统的典型工程经验。
