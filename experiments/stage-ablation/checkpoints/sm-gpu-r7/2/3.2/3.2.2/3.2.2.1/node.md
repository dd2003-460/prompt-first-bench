# N141: KV Cache 大小计算中 bytes_per_element 取决于 KV Cache 的量化精度，若与权重精度一致则为 2 bytes (BF16)，若 

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N39

## Claim

KV Cache 大小计算中 bytes_per_element 取决于 KV Cache 的量化精度，若与权重精度一致则为 2 bytes (BF16)，若 KV Cache 单独量化为 INT8 则为 1 byte，若为 FP8 则为 1 byte，需明确假设精度以计算具体数值

## Corrected Claim

KV Cache 大小计算中 bytes_per_element 取决于 KV Cache 的量化精度，若与权重精度一致则为 2 bytes (BF16)，若 KV Cache 单独量化为 INT8 则为 1 byte，若为 FP8 则为 1 byte，需明确假设精度以计算具体数值

## Evidence

先验知识/题面给定，逻辑校验通过
