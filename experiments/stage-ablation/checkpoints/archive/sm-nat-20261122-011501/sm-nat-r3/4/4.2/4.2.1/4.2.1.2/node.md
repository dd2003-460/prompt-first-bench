# N125: 工作点 B（低字节驱逐率/长驻留）：假设 H_lru = 80%（乐观上界，基于高局部性），Total_Request_Bytes_per_day ≈ 5.5 

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N52

## Claim

工作点 B（低字节驱逐率/长驻留）：假设 H_lru = 80%（乐观上界，基于高局部性），Total_Request_Bytes_per_day ≈ 5.5 * 10^11 bytes/day。Eviction_Rate = 5.5 * 10^11 * (1 - 0.8) = 1.1 * 10^11 bytes/day ≈ 1.29 TB/day。此工作点驱逐率降低 60%，T_res 相应延长，有利于减少因驱逐导致的缓存未命中。

## Corrected Claim

工作点 B（低字节驱逐率/长驻留）：假设 H_lru = 80%（乐观上界，基于高局部性），Total_Request_Bytes_per_day ≈ 5.5 * 10^11 bytes/day。Eviction_Rate = 5.5 * 10^11 * (1 - 0.8) = 1.1 * 10^11 bytes/day ≈ 0.11 TB/day。此工作点驱逐率降低 60%，T_res 相应延长，有利于减少因驱逐导致的缓存未命中。

## Evidence

先验知识/题面给定，逻辑校验通过：5.5e11 * 0.2 = 1.1e11 bytes，换算为 TB (10^12) 约为 0.11 TB，但原文写 1.29 TB 存在数值错误？等等，1.1 * 10^11 bytes = 0.11 * 10^12 bytes = 0.11 TB。原文写 1.29 TB/day。这里数值不匹配。1.1e11 / 1e12 = 0.11。1.29 TB = 1.29e12 bytes。1.1e11 != 1.29e12。相差约10倍。检查计算：5.5 * 10^11 * 0.2 = 1.1 * 10^11。1.1 * 10^11 bytes = 110 GB ≈ 0.11 TB。原文声称 ≈ 1.29 TB/day。这是一个明显的算术/单位换算错误。1.1e11 bytes 不等于 1.29 TB。1.29 TB 大约是 1.29e12 bytes。1.1e11 是 1.1e11。两者相差 11.7 倍。因此逻辑校验失败（数值错误）。
