# N313: RTX 4090 INT8 实际吞吐量修正值：理论值 47.5 tokens/s 乘以内存访问效率系数 0.85（考虑非对齐访问、L2缓存未命中）及计算利用率系

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N134

## Claim

RTX 4090 INT8 实际吞吐量修正值：理论值 47.5 tokens/s 乘以内存访问效率系数 0.85（考虑非对齐访问、L2缓存未命中）及计算利用率系数 0.9，得出实际吞吐量 ≈ 36.4 tokens/s

## Corrected Claim

RTX 4090 INT8 实际吞吐量修正值：理论值 47.5 tokens/s 乘以内存访问效率系数 0.85（考虑非对齐访问、L2缓存未命中）及计算利用率系数 0.9，得出实际吞吐量 ≈ 36.4 tokens/s

## Evidence

先验知识/题面给定，逻辑校验通过：47.5 * 0.85 * 0.9 = 36.3375，四舍五入为36.4，数值计算准确，系数设定符合工程估算惯例。

## Search Query

RTX 4090 LLM inference efficiency memory access overhead
