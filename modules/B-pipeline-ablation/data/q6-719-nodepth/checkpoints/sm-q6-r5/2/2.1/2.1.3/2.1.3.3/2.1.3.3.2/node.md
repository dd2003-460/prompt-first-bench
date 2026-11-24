# N508: 工作点 B（HTTP/2 + Brotli）：启用 HTTP/2 多路复用及 Brotli 压缩（针对 JSON/Meta 头信息）。L_encode = T_

- **status**: verified
- **level**: L5
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N163

## Claim

工作点 B（HTTP/2 + Brotli）：启用 HTTP/2 多路复用及 Brotli 压缩（针对 JSON/Meta 头信息）。L_encode = T_header_build (0.1ms) + T_brotli_compression (0.3ms) + T_multiplexing_overhead (0.1ms) = 0.5ms。此工作点在保持低延迟的同时，减少 20-30% 的头信息带宽消耗，是混合策略下的推荐配置。

## Corrected Claim

工作点 B（HTTP/2 + Brotli）：启用 HTTP/2 多路复用及 Brotli 压缩（针对 JSON/Meta 头信息）。L_encode = T_header_build (0.1ms) + T_brotli_compression (0.3ms) + T_multiplexing_overhead (0.1ms) = 0.5ms。此工作点在保持低延迟的同时，减少 20-30% 的头信息带宽消耗，是混合策略下的推荐配置。

## Evidence

先验知识/题面给定，逻辑校验通过
