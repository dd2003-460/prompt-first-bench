# N154: LFU 对长尾对象（请求频率 < 0.95 分位数）的误保留字节量 B_lfu_tail = N_total * (1 - F_freq(0.95)) * E[

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N52

## Claim

LFU 对长尾对象（请求频率 < 0.95 分位数）的误保留字节量 B_lfu_tail = N_total * (1 - F_freq(0.95)) * E[size|tail] * r_tail，需计算 F_freq(0.95) 对应的频率阈值 r_95 及该区间内的平均大小与频率

## Corrected Claim

LFU 对长尾对象（请求频率 < 0.95 分位数）的误保留字节量 B_lfu_tail = N_total * (1 - F_freq(0.95)) * E[size|tail] * r_tail，需计算 F_freq(0.95) 对应的频率阈值 r_95 及该区间内的平均大小与频率

## Evidence

先验知识/题面给定，逻辑校验通过
