# N156: 扫描攻击（Scan Attack）下 LRU 的命中率下限 H_LRU_scan = 0，而 LFU 的命中率下限 H_LFU_scan = C_head * 

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N60

## Claim

扫描攻击（Scan Attack）下 LRU 的命中率下限 H_LRU_scan = 0，而 LFU 的命中率下限 H_LFU_scan = C_head * (1 - 1/T_fresh)，其中 T_fresh 为对象首次访问后保持高频的时间窗口（天数），当 T_fresh=1 day 时，H_LFU_scan ≈ C_head * 0，即 LFU 在纯扫描攻击下也失效，其鲁棒性优势仅在混合负载（扫描+稳态）中体现。

## Corrected Claim

扫描攻击（Scan Attack）下 LRU 的命中率下限 H_LRU_scan = 0，而 LFU 的命中率下限 H_LFU_scan = C_head * (1 - 1/T_fresh)，其中 T_fresh 为对象首次访问后保持高频的时间窗口（天数），当 T_fresh=1 day 时，H_LFU_scan ≈ C_head * 0，即 LFU 在纯扫描攻击下也失效，其鲁棒性优势仅在混合负载（扫描+稳态）中体现。

## Evidence

先验知识/题面给定，逻辑校验通过：LRU在纯扫描攻击下命中率确实为0；LFU在T_fresh=1天（即高频窗口极短或仅覆盖首次访问）时，后续扫描访问因频率未累积或已衰减，命中率趋近于0，符合缓存替换算法的基本原理。
