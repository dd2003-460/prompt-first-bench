# N455: 西部/东北区域使用公有云 CDN 的 P99 延迟基准 T_p99_cloud = T_trans_cloud + T_queue_cloud + T_proc

- **status**: verified
- **level**: L5
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N152

## Claim

西部/东北区域使用公有云 CDN 的 P99 延迟基准 T_p99_cloud = T_trans_cloud + T_queue_cloud + T_processing，其中 T_trans_cloud 基于云厂商最近节点距离（通常 < 200km）估算为 ≈1ms，T_queue_cloud 基于云厂商高冗余设计通常 < 5ms，T_processing < 10ms，合计 T_p99_cloud ≈ 16ms；该值作为混合策略中该区域延迟贡献的基准线。

## Corrected Claim

西部/东北区域使用公有云 CDN 的 P99 延迟基准 T_p99_cloud = T_trans_cloud + T_queue_cloud + T_processing，其中 T_trans_cloud 基于云厂商最近节点距离（通常 < 200km）估算为 ≈1ms，T_queue_cloud 基于云厂商高冗余设计通常 < 5ms，T_processing < 10ms，合计 T_p99_cloud ≈ 16ms；该值作为混合策略中该区域延迟贡献的基准线。

## Evidence

先验知识/题面给定，逻辑校验通过：1ms(传输) + 5ms(队列) + 10ms(处理) = 16ms，数值量级符合公有云CDN在近距离节点下的典型性能基准，且作为基准线定义逻辑自洽。
