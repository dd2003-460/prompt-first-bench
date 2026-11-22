# N15: LRU 稳态驻留时间 T_res 的量化：对于 128GB 缓存和 5000 万次/天请求，假设热门对象平均大小 S_hot，T_res ≈ C / (R * 

- **status**: degraded
- **level**: L2
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N4

## Claim

LRU 稳态驻留时间 T_res 的量化：对于 128GB 缓存和 5000 万次/天请求，假设热门对象平均大小 S_hot，T_res ≈ C / (R * S_hot * (1 - H_lru))，其中 H_lru 是基础命中率。

## Corrected Claim

LRU 稳态驻留时间 T_res 的量化：对于 128GB 缓存和 5000 万次/天请求，假设热门对象平均大小 S_hot，T_res 应基于访问频率分布计算，例如 T_res ≈ 1 / (R * P_access)，其中 P_access 为对象被访问的概率密度，而非 C / (R * S_hot * (1 - H_lru))。

## Evidence

[质询]公式量纲与逻辑不自洽：T_res 通常指时间（秒/天），而公式右侧 C/(R*S_hot*(1-H_lru)) 中，若 C 为缓存容量（字节），R 为请求率（次/秒），S_hot 为对象大小（字节），则分母量纲为 字节²/秒，整体量纲为 秒/字节²，无法得出时间单位；且 LRU 驻留时间通常由访问频率倒数决定，而非直接由缓存容量和命中率通过此特定代数式推导。 | 先验知识/题面给定，但逻辑校验发现量纲错误（时间 vs 秒/字节²）及物理直觉违背（驻留时间不应随缓存容量线性增加而随命中率降低而增加，且公式结构不符合 LRU 替换策略的基本数学模型），故降级。

## Search Query

LRU cache residence time formula
