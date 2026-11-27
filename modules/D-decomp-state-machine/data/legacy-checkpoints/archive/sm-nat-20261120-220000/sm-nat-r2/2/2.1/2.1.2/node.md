# N28: LFU在β=0.9下的性能优势源于其频率计数机制对头部稳定高频对象的锁定效应，具体表现为：当对象访问频率稳定时，LFU的缓存驻留时间 T_resident_LF

- **status**: degraded
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N8

## Claim

LFU在β=0.9下的性能优势源于其频率计数机制对头部稳定高频对象的锁定效应，具体表现为：当对象访问频率稳定时，LFU的缓存驻留时间 T_resident_LFU ≈ N_requests / f_i，而LRU的 T_resident_LRU ≈ 1/f_i * C/N_objects，两者比值 R = (N_requests/N_objects) / (C/N_objects) = N_requests/C，在C=128GB且S_total≈11.1MB时，R极大，说明LFU在理论上能更稳定地保留头部对象，从而提升命中率

## Corrected Claim

LFU在β=0.9下的性能优势源于其频率计数机制对头部稳定高频对象的锁定效应。具体表现为：当对象访问频率稳定且远高于其他对象时，LFU能更有效地将缓存空间分配给这些高频对象，从而提升命中率。但具体的驻留时间公式需结合缓存容量、对象大小及竞争频率分布进行更严谨的建模，原陈述中的简化公式存在量纲错误。

## Evidence

[质询]公式推导存在严重的量纲错误和逻辑谬误。1. T_resident_LFU ≈ N_requests / f_i 的量纲是 [时间]（若f_i是频率）或 [次数]（若f_i是概率），而 T_resident_LRU ≈ 1/f_i * C/N_objects 的量纲混乱（C/N_objects是大小比，无量纲或长度，乘以1/f_i后量纲不统一）。2. 比值 R = N_requests/C 中，N_requests是次数，C是容量（GB），两者相除无物理意义。3. LFU的驻留时间并不直接等于总请求数除以频率，而是取决于缓存替换策略和竞争对象的频率分布，该简化公式忽略了缓存容量限制和对象大小差异，属于错误的理论推导。 | 先验知识/题面给定，逻辑校验失败：公式量纲不一致，且LFU驻留时间的简化推导违背缓存替换基本逻辑（未考虑容量约束和对象大小），属于硬逻辑错误。
