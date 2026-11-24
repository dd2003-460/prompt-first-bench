# N43: 自建 10 POP 点 P99=200ms 的构成拆解：T_self = T_last_mile + T_edge_processing_self + T_or

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N8

## Claim

自建 10 POP 点 P99=200ms 的构成拆解：T_self = T_last_mile + T_edge_processing_self + T_origin_fallback_self，其中 T_last_mile 与公有云相同 (50-80ms)，T_edge_processing_self 因硬件性能略高于公有云 (15-30ms)，T_origin_fallback_self = (1-CHR_self) * T_origin_self，T_origin_self 因回源距离长 (跨省/跨区) 典型值 150-300ms

## Corrected Claim

自建 10 POP 点 P99=200ms 的构成拆解：T_self = T_last_mile + T_edge_processing_self + T_origin_fallback_self，其中 T_last_mile 与公有云相同 (50-80ms)，T_edge_processing_self 因硬件性能略高于公有云 (15-30ms)，T_origin_fallback_self = (1-CHR_self) * T_origin_self，T_origin_self 因回源距离长 (跨省/跨区) 典型值 150-300ms

## Evidence

先验知识/题面给定，逻辑校验通过：P99延迟构成拆解符合网络传输基本逻辑，各分项数值量级（最后一公里50-80ms、边缘处理15-30ms、回源150-300ms）在自建POP场景下合理且自洽。

## Search Query

Self-hosted CDN edge node P99 latency breakdown origin fallback distance impact
