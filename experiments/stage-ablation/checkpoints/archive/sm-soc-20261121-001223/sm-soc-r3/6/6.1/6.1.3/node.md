# N192: T_lag 对买家可见性的阈值效应：定义 T_visible = T_lag + T_network_latency；若 T_visible > T_buyer

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N70

## Claim

T_lag 对买家可见性的阈值效应：定义 T_visible = T_lag + T_network_latency；若 T_visible > T_buyer_session_duration（买家单次会话平均时长，如 5-10 分钟），则买家在降价后短时间内无法看到新价格，导致咨询量延迟；需量化 T_visible 与 T_buyer_session_duration 的比值分布，若中位数 > 2.0，则支持‘延迟导致无咨询’假设。

## Corrected Claim

T_lag 对买家可见性的阈值效应：定义 T_visible = T_lag + T_network_latency；若 T_visible > T_buyer_session_duration（买家单次会话平均时长，如 5-10 分钟），则买家在降价后短时间内无法看到新价格，导致咨询量延迟；需量化 T_visible 与 T_buyer_session_duration 的比值分布，若中位数 > 2.0，则支持‘延迟导致无咨询’假设。

## Evidence

先验知识/题面给定，逻辑校验通过
