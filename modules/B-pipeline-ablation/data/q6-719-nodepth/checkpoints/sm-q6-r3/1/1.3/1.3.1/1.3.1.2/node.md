# N163: T_processing（CPU 处理时间）主要消耗在 TLS 握手与解密、HTTP 解析及缓存键哈希计算上，典型值 0.1-1ms；若启用硬件加速（如 AES

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N46

## Claim

T_processing（CPU 处理时间）主要消耗在 TLS 握手与解密、HTTP 解析及缓存键哈希计算上，典型值 0.1-1ms；若启用硬件加速（如 AES-NI），TLS 开销可降低至 0.05ms，否则纯软件实现约为 0.5-1ms

## Corrected Claim

T_processing（CPU 处理时间）主要消耗在 TLS 握手与解密、HTTP 解析及缓存键哈希计算上，典型值 0.1-1ms；若启用硬件加速（如 AES-NI），TLS 开销可降低至 0.05ms，否则纯软件实现约为 0.5-1ms

## Evidence

先验知识/题面给定，逻辑校验通过
