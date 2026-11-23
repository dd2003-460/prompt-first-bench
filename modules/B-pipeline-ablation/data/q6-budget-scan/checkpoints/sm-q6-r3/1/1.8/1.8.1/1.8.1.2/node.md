# N232: 核心区域 T_proc_P99(j) 的构成：T_proc_P99(j) = T_cache_lookup + T_tcp_handshake + T_http

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N72

## Claim

核心区域 T_proc_P99(j) 的构成：T_proc_P99(j) = T_cache_lookup + T_tcp_handshake + T_http_processing，其中 T_cache_lookup ≈ 0.1-0.5ms（内存查找），T_tcp_handshake ≈ 1 RTT（若启用 TLS 则 1.5 RTT），T_http_processing ≈ 1-5ms（应用层处理），总计约 2-10ms（不含 RTT）

## Corrected Claim

核心区域 T_proc_P99(j) 的构成：T_proc_P99(j) = T_cache_lookup + T_tcp_handshake + T_http_processing，其中 T_cache_lookup ≈ 0.1-0.5ms（内存查找），T_tcp_handshake ≈ 1 RTT（若启用 TLS 则 1.5 RTT），T_http_processing ≈ 1-5ms（应用层处理），总计约 2-10ms（不含 RTT）

## Evidence

先验知识/题面给定，逻辑校验通过

## Search Query

CDN edge server processing time cache lookup latency
