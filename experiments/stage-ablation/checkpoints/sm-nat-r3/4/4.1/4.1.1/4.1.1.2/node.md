# N128: 分层驻留时间 T_LRU_i 的修正公式：对于排名 i 的对象，其被替换的概率取决于其栈距离。在稳态 LRU 中，若缓存未溢出（N < K_capacity），

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N54

## Claim

分层驻留时间 T_LRU_i 的修正公式：对于排名 i 的对象，其被替换的概率取决于其栈距离。在稳态 LRU 中，若缓存未溢出（N < K_capacity），所有对象驻留时间为无穷大（或系统运行时间），T_LRU_i → ∞。若缓存溢出，T_LRU_i ≈ 1 / (λ_i * P_replace)，其中 P_replace 为被更热门对象替换的概率。

## Corrected Claim

分层驻留时间 T_LRU_i 的修正公式：对于排名 i 的对象，其被替换的概率取决于其栈距离。在稳态 LRU 中，若缓存未溢出（N < K_capacity），所有对象驻留时间为无穷大（或系统运行时间），T_LRU_i → ∞。若缓存溢出，T_LRU_i ≈ 1 / (λ_i * P_replace)，其中 P_replace 为被更热门对象替换的概率。

## Evidence

先验知识/题面给定，逻辑校验通过

## Search Query

LRU cache residency time formula stack distance steady state
