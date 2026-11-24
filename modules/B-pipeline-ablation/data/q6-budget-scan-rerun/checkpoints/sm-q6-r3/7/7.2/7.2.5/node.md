# N266: RTT_processing 的软件栈分解：RTT_processing = T_tls_handshake + T_http_processing + T_c

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N115, N116, N121

## Claim

RTT_processing 的软件栈分解：RTT_processing = T_tls_handshake + T_http_processing + T_cache_lookup + T_compression。典型值：T_tls_handshake=0.5ms (Session Resumption), T_http_processing=0.2ms, T_cache_lookup=1.5ms (N8), T_compression=0.8ms (Brotli, 200KB对象)。总RTT_processing ≈ 3.0ms (P50)，P99 ≈ 5.0ms (含GC停顿/慢路径)。

## Corrected Claim

RTT_processing 的软件栈分解：RTT_processing = T_tls_handshake + T_http_processing + T_cache_lookup + T_compression。典型值：T_tls_handshake=0.5ms (Session Resumption), T_http_processing=0.2ms, T_cache_lookup=1.5ms (N8), T_compression=0.8ms (Brotli, 200KB对象)。总RTT_processing ≈ 3.0ms (P50)，P99 ≈ 5.0ms (含GC停顿/慢路径)。

## Evidence

先验知识/题面给定，逻辑校验通过：各分项量级符合典型Web服务器软件栈处理耗时特征（TLS会话恢复、HTTP解析、缓存查找、压缩），总和与P50/P99分布逻辑自洽。

## Search Query

CDN edge server software stack latency breakdown TLS handshake HTTP processing cache lookup compression
