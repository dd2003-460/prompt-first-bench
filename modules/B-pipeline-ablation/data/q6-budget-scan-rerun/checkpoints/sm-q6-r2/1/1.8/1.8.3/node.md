# N69: T_process_self 的量化分解：自建服务器处理延迟包括内核协议栈开销（2-5ms）、用户态缓存查找（<1ms）、SSL 解密（1-3ms），P99 贡

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N13

## Claim

T_process_self 的量化分解：自建服务器处理延迟包括内核协议栈开销（2-5ms）、用户态缓存查找（<1ms）、SSL 解密（1-3ms），P99 贡献典型值为 5-15ms，低于公有云因无虚拟化开销

## Corrected Claim

T_process_self 的量化分解：自建服务器处理延迟包括内核协议栈开销（2-5ms）、用户态缓存查找（<1ms）、SSL 解密（1-3ms），P99 贡献典型值为 5-15ms，低于公有云因无虚拟化开销

## Evidence

先验知识/题面给定，逻辑校验通过

## Search Query

Self-built server processing latency kernel protocol stack SSL decryption P99
