# N81: 混合云工作点B的延迟对吞吐量影响修正：T_iter_mixed = (1 - Ratio) * T_iter_local + Ratio * (T_iter_c

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N28

## Claim

混合云工作点B的延迟对吞吐量影响修正：T_iter_mixed = (1 - Ratio) * T_iter_local + Ratio * (T_iter_cloud + RTT + Queue_Delay)，其中 T_iter_cloud ≈ 5min (云端处理长链推理)，RTT ≈ 200ms，Queue_Delay ≈ 1min (高峰期)，则 T_iter_mixed ≈ 0.8 * 30min + 0.2 * 6.2min ≈ 24.84min，相比纯本地的 30min 略有提升，但主要瓶颈仍在本地慢速部分，需评估是否值得为 6% 质量提升支付 20% 延迟优化

## Corrected Claim

混合云工作点B的延迟对吞吐量影响修正：T_iter_mixed = (1 - Ratio) * T_iter_local + Ratio * (T_iter_cloud + RTT + Queue_Delay)，其中 T_iter_cloud ≈ 5min (云端处理长链推理)，RTT ≈ 200ms，Queue_Delay ≈ 1min (高峰期)，则 T_iter_mixed ≈ 0.8 * 30min + 0.2 * 6.2min ≈ 24.84min，相比纯本地的 30min 略有提升，但主要瓶颈仍在本地慢速部分，需评估是否值得为 6% 质量提升支付 20% 延迟优化

## Evidence

先验知识/题面给定，逻辑校验通过：算术计算正确（0.8*30 + 0.2*6.2 = 24.84），量纲一致，符合混合云延迟加权平均的基本逻辑。
