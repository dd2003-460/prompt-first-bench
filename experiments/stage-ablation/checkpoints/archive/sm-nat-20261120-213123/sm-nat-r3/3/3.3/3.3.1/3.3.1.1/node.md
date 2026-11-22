# N115: LRU 稳态周转时间 T_LRU 在‘头部对象主导’工作点（Top-1% 对象）的数值：假设 Top-1000 对象占据 95% 请求且平均大小 5KB，总字节

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N47

## Claim

LRU 稳态周转时间 T_LRU 在‘头部对象主导’工作点（Top-1% 对象）的数值：假设 Top-1000 对象占据 95% 请求且平均大小 5KB，总字节流 R_byte ≈ 5000万 * 5KB = 2.5e11 bytes/天，T_LRU ≈ 128GB / (R_byte * 0.95) ≈ 0.53 天，表明热门对象在缓存中停留时间极短。

## Corrected Claim

LRU 稳态周转时间 T_LRU 在‘头部对象主导’工作点（Top-1% 对象）的数值：假设 Top-1000 对象占据 95% 请求且平均大小 5KB，总字节流 R_byte ≈ 5000万 * 5KB = 2.5e11 bytes/天，T_LRU ≈ 128GB / (R_byte * 0.95) ≈ 0.53 天，表明热门对象在缓存中停留时间极短。

## Evidence

先验知识/题面给定，逻辑校验通过：数值计算准确（128GB / (2.5e11 * 0.95) ≈ 0.53天），量纲与物理直觉一致，符合LRU缓存周转时间定义。
