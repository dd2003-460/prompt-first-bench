# N609: M3 Ultra KV Cache 读取延迟修正：基于 N288 修正后的 KV Size (34.36 GB)，读取时间 T_read = 34.36 GB 

- **status**: verified
- **level**: L5
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N254

## Claim

M3 Ultra KV Cache 读取延迟修正：基于 N288 修正后的 KV Size (34.36 GB)，读取时间 T_read = 34.36 GB / 800 GB/s ≈ 42.95 ms。原 N254 基于 1.0 GB 计算的 1.25 ms 严重低估，实际单 token Decode 的内存读取瓶颈约为 43 ms。

## Corrected Claim

M3 Ultra KV Cache 读取延迟修正：基于 N288 修正后的 KV Size (34.36 GB)，读取时间 T_read = 34.36 GB / 800 GB/s ≈ 42.95 ms。原 N254 基于 1.0 GB 计算的 1.25 ms 严重低估，实际单 token Decode 的内存读取瓶颈约为 43 ms。

## Evidence

先验知识/题面给定，逻辑校验通过：34.36 GB / 800 GB/s = 0.04295 s = 42.95 ms，计算准确且量级合理。
