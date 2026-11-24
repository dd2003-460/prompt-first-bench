# N84: 公有云弹性响应时间 T_scale_pub 对 P99 延迟的影响机制：虽然厂商响应时间为 1-5 分钟，但在突发流量下，若扩容未完成，请求将排队或触发限流，导

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N20

## Claim

公有云弹性响应时间 T_scale_pub 对 P99 延迟的影响机制：虽然厂商响应时间为 1-5 分钟，但在突发流量下，若扩容未完成，请求将排队或触发限流，导致 P99 延迟激增。量化影响：若扩容延迟 T_delay=5min，期间超出容量的请求比例 P_overflow = (B_actual - B_current_capacity) / B_actual。假设突发流量为平均的 4 倍，且当前容量为 3 倍平均，则 P_overflow 约为 25%，这部分请求的延迟可能超过 T=300ms，需计入 SLA 赔付风险成本。

## Corrected Claim

公有云弹性响应时间 T_scale_pub 对 P99 延迟的影响机制：虽然厂商响应时间为 1-5 分钟，但在突发流量下，若扩容未完成，请求将排队或触发限流，导致 P99 延迟激增。量化影响：若扩容延迟 T_delay=5min，期间超出容量的请求比例 P_overflow = (B_actual - B_current_capacity) / B_actual。假设突发流量为平均的 4 倍，且当前容量为 3 倍平均，则 P_overflow 约为 25%，这部分请求的延迟可能超过 T=300ms，需计入 SLA 赔付风险成本。

## Evidence

先验知识/题面给定，逻辑校验通过：数学推导正确（(4-3)/4=25%），机制描述符合公有云弹性扩容的通用工程原理。

## Search Query

cloud auto-scaling delay impact on latency percentile
