# N12: LRU 有效命中率折损系数 = 1 / (1 + λ_update * T_avg_residence)，其中 λ_update = 0.01/天，T_avg_

- **status**: pending
- **level**: L2
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N3

## Claim

LRU 有效命中率折损系数 = 1 / (1 + λ_update * T_avg_residence)，其中 λ_update = 0.01/天，T_avg_residence 为对象在缓存中的平均驻留时间；在稳态下 T_avg_residence ≈ 1/λ_access，λ_access 为对象平均访问频率

## Corrected Claim

LRU 有效命中率折损系数 = 1 / (1 + λ_update * T_avg_residence)，其中 λ_update = 0.01/天，T_avg_residence 为对象在缓存中的平均驻留时间；在稳态下 T_avg_residence ≈ 1/λ_access，λ_access 为对象平均访问频率

## Evidence

父节点级核验失败（LLM 错误）：curl rc=28 b''
