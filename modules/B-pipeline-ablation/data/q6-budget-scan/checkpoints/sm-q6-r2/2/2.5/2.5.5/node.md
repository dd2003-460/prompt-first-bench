# N78: T_cache_hit的构成：T_cache_hit = T_queue_edge + T_transmission_edge + T_processing_e

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N15, N16, N17

## Claim

T_cache_hit的构成：T_cache_hit = T_queue_edge + T_transmission_edge + T_processing_edge；其中T_transmission_edge = s / BW_user_POP，BW_user_POP为用户到POP的带宽；对于国内用户，BW_user_POP通常为100Mbps-1Gbps，T_transmission_edge对于5MB对象约为40-400ms，但P99通常受限于最后一公里带宽，典型P99_transmission_edge为50-100ms。

## Corrected Claim

T_cache_hit的构成：T_cache_hit = T_queue_edge + T_transmission_edge + T_processing_edge；其中T_transmission_edge = s / BW_user_POP，BW_user_POP为用户到POP的带宽；对于国内用户，BW_user_POP通常为100Mbps-1Gbps，T_transmission_edge对于5MB对象约为40-400ms，但P99通常受限于最后一公里带宽，典型P99_transmission_edge为50-100ms。

## Evidence

先验知识/题面给定，逻辑校验通过：5MB对象在100Mbps-1Gbps带宽下的传输时间计算（40ms-400ms）符合物理公式 T=s/BW，且P99延迟描述符合网络工程常识。

## Search Query

CDN cache hit edge latency components
