# N431: 上海本地场景下CDN节点软件处理延迟 T_processing 的构成：T_processing = T_lookup + T_auth + T_encodin

- **status**: verified
- **level**: L5
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N145

## Claim

上海本地场景下CDN节点软件处理延迟 T_processing 的构成：T_processing = T_lookup + T_auth + T_encoding_check，典型值 1-5ms，主要受缓存命中率影响（命中时 T_lookup < 1ms，未命中时 T_lookup > 10ms 因需回源）

## Corrected Claim

上海本地场景下CDN节点软件处理延迟 T_processing 的构成：T_processing = T_lookup + T_auth + T_encoding_check，典型值 1-5ms，主要受缓存命中率影响（命中时 T_lookup < 1ms，未命中时 T_lookup > 10ms 因需回源）

## Evidence

先验知识/题面给定，逻辑校验通过

## Search Query

CDN edge server processing latency cache hit miss breakdown
