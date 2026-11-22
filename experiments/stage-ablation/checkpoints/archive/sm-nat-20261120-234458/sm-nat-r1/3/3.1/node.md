# N12: LRU 有效命中率折损系数 = 1 / (1 + λ_update * T_avg_residence)，其中 λ_update = 0.01/天，T_avg_

- **status**: verified
- **level**: L2
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N3

## Claim

LRU 有效命中率折损系数 = 1 / (1 + λ_update * T_avg_residence)，其中 λ_update = 0.01/天，T_avg_residence 为对象在缓存中的平均驻留时间；在稳态下 T_avg_residence ≈ 1/λ_access，λ_access 为对象平均访问频率

## Corrected Claim

LRU 有效命中率折损系数 = 1 / (1 + λ_update * T_avg_residence)，其中 λ_update = 0.01/天，T_avg_residence 为对象在缓存中的平均驻留时间；在稳态下 T_avg_residence ≈ 1/λ_access，λ_access 为对象平均访问频率

## Evidence

先验知识/题面给定，逻辑校验通过：LRU缓存中对象被更新导致失效的概率与更新频率及驻留时间成正比，稳态下驻留时间由访问频率决定，公式推导符合排队论与缓存失效的基本逻辑。
