# N43: 算术强度(Arithmetic Intensity)计算：AI = FLOPs/MemBytes = 2*P / (P + KV_cache_read)。在长上

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N10

## Claim

算术强度(Arithmetic Intensity)计算：AI = FLOPs/MemBytes = 2*P / (P + KV_cache_read)。在长上下文(262k)下，KV读取占主导，AI < 1，处于内存带宽受限区(Memory-bound)

## Corrected Claim

算术强度(Arithmetic Intensity)计算：AI = FLOPs/MemBytes = 2*P / (P + KV_cache_read)。在长上下文(262k)下，KV读取占主导，AI < 1，处于内存带宽受限区(Memory-bound)

## Evidence

先验知识/题面给定，逻辑校验通过：根据Roofline模型定义，AI=FLOPs/MemBytes。对于Transformer解码阶段，每生成一个token需读取整个KV Cache（大小随序列长度线性增长），而计算量相对固定或增长较慢，因此在长上下文（262k）下，内存访问字节数远大于计算量对应的等效字节数，导致AI<1，处于Memory-bound区域，符合计算机体系结构基本原理。
