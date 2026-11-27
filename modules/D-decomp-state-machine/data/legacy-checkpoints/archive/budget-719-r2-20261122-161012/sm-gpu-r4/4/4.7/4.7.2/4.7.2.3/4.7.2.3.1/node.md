# N611: RTX 4090 KV Cache 读取延迟修正：基于 N288 修正后的 KV Size (34.36 GB)，读取时间 T_read = 34.36 GB 

- **status**: verified
- **level**: L5
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N255

## Claim

RTX 4090 KV Cache 读取延迟修正：基于 N288 修正后的 KV Size (34.36 GB)，读取时间 T_read = 34.36 GB / 1008 GB/s ≈ 34.1 ms。原 N255 基于 1.0 GB 计算的 0.99 ms 严重低估，实际单 token Decode 的内存读取瓶颈约为 34 ms。

## Corrected Claim

RTX 4090 KV Cache 读取延迟修正：基于 N288 修正后的 KV Size (34.36 GB)，读取时间 T_read = 34.36 GB / 1008 GB/s ≈ 34.1 ms。原 N255 基于 1.0 GB 计算的 0.99 ms 严重低估，实际单 token Decode 的内存读取瓶颈约为 34 ms。

## Evidence

先验知识/题面给定，逻辑校验通过：34.36 GB / 1008 GB/s ≈ 0.0341 s = 34.1 ms，计算无误且量级合理。
