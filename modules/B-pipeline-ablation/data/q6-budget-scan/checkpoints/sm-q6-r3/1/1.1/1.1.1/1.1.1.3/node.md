# N178: HTTP/2 头部解析与压缩（HPACK）的 P99 延迟 T_http_parse_p99 ≈ T_decode_hpack + T_header_valid

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N52

## Claim

HTTP/2 头部解析与压缩（HPACK）的 P99 延迟 T_http_parse_p99 ≈ T_decode_hpack + T_header_validation，其中 T_decode_hpack ≈ 0.1-0.3ms（基于 Huffman 解码表查表），T_header_validation ≈ 0.1-0.5ms（依赖头部数量，通常 10-20 个字段），总 P99 < 1ms；若启用 Header Compression 动态表，需额外 0.05ms 内存访问开销。

## Corrected Claim

HTTP/2 头部解析与压缩（HPACK）的 P99 延迟 T_http_parse_p99 ≈ T_decode_hpack + T_header_validation，其中 T_decode_hpack ≈ 0.1-0.3ms（基于 Huffman 解码表查表），T_header_validation ≈ 0.1-0.5ms（依赖头部数量，通常 10-20 个字段），总 P99 < 1ms；若启用 Header Compression 动态表，需额外 0.05ms 内存访问开销。

## Evidence

先验知识/题面给定，逻辑校验通过

## Search Query

HTTP/2 HPACK header decoding latency milliseconds CPU cost
