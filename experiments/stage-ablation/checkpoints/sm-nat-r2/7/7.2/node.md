# N94: LRU 稳态下保护头部 10-20% 对象的容量匹配条件：设头部 10% 对象的总字节量为 S_top10 = 0.1 * N * E[S | top 10%]

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N31

## Claim

LRU 稳态下保护头部 10-20% 对象的容量匹配条件：设头部 10% 对象的总字节量为 S_top10 = 0.1 * N * E[S | top 10%]，头部 20% 对象的总字节量为 S_top20 = 0.2 * N * E[S | top 20%]；LRU 能完整保护头部 10% 对象的条件是 S_top10 ≤ 128GB，即 E[S | top 10%] ≤ 12.8KB；若 S_top10 > 128GB，则 LRU 无法完整保护头部 10% 对象，字节命中率下界需进一步修正。

## Corrected Claim

LRU 稳态下保护头部 10-20% 对象的容量匹配条件：设头部 10% 对象的总字节量为 S_top10 = 0.1 * N * E[S | top 10%]，头部 20% 对象的总字节量为 S_top20 = 0.2 * N * E[S | top 20%]；LRU 能完整保护头部 10% 对象的条件是 S_top10 ≤ 128GB，即 E[S | top 10%] ≤ 12.8KB；若 S_top10 > 128GB，则 LRU 无法完整保护头部 10% 对象，字节命中率下界需进一步修正。

## Evidence

先验知识/题面给定，逻辑校验通过：LRU 保护头部对象的前提是缓存容量足以容纳该部分对象的总大小，数学推导自洽。
