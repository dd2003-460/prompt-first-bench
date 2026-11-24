# N135: T_processing 计算模型：T_proc = t_tls_handshake + t_decompress + t_encode，其中 t_tls_ha

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N39

## Claim

T_processing 计算模型：T_proc = t_tls_handshake + t_decompress + t_encode，其中 t_tls_handshake 为 TLS 1.3 握手耗时（典型值 1-3ms/连接，若复用连接则为 0），t_decompress 为内容解压耗时（基于 CPU 单核性能，100MB/s 吞吐下 1MB 对象解压约 10ms），t_encode 为编码/转码耗时（若边缘无转码则为 0）；缓存命中场景下 T_proc ≈ 5-15ms，回源场景下 T_proc ≈ 20-50ms。

## Corrected Claim

T_processing 计算模型：T_proc = t_tls_handshake + t_decompress + t_encode，其中 t_tls_handshake 为 TLS 1.3 握手耗时（典型值 1-3ms/连接，若复用连接则为 0），t_decompress 为内容解压耗时（基于 CPU 单核性能，100MB/s 吞吐下 1MB 对象解压约 10ms），t_encode 为编码/转码耗时（若边缘无转码则为 0）；缓存命中场景下 T_proc ≈ 5-15ms，回源场景下 T_proc ≈ 20-50ms。

## Evidence

先验知识/题面给定，逻辑校验通过
