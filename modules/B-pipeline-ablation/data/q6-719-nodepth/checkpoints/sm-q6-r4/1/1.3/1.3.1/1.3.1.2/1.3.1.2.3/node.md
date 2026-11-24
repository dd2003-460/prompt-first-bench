# N487: HTTP 解析与缓存键哈希开销分解：T_http_hash = T_parse + T_hash，其中 T_parse ≈ 0.05ms (解析 HTTP/1.

- **status**: verified
- **level**: L5
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N163

## Claim

HTTP 解析与缓存键哈希开销分解：T_http_hash = T_parse + T_hash，其中 T_parse ≈ 0.05ms (解析 HTTP/1.1 头部平均 500 字节)，T_hash ≈ 0.01ms (MD5/SHA1 哈希 64 字节 URL 键)，合计 0.06ms，为 T_processing 次要项

## Corrected Claim

HTTP 解析与缓存键哈希开销分解：T_http_hash = T_parse + T_hash，其中 T_parse ≈ 0.05ms (解析 HTTP/1.1 头部平均 500 字节)，T_hash ≈ 0.01ms (MD5/SHA1 哈希 64 字节 URL 键)，合计 0.06ms，为 T_processing 次要项

## Evidence

先验知识/题面给定，逻辑校验通过
