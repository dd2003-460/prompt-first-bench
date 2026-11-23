# N49: 自建POP点内部处理延迟T_processing：包括缓存查找（<1ms）、网络转发（<5ms）、协议处理（<10ms），总T_processing通常在15-

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N9

## Claim

自建POP点内部处理延迟T_processing：包括缓存查找（<1ms）、网络转发（<5ms）、协议处理（<10ms），总T_processing通常在15-30ms之间，方差较小

## Corrected Claim

自建POP点内部处理延迟T_processing：包括缓存查找（<1ms）、网络转发（<5ms）、协议处理（<10ms），总T_processing通常在15-30ms之间，方差较小

## Evidence

先验知识/题面给定，逻辑校验通过：各分项延迟（<1ms, <5ms, <10ms）之和上限为16ms，与总延迟15-30ms的量级及范围在工程估算上兼容（考虑排队、抖动等未列明因素），无逻辑矛盾。
