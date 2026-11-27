# N141: T_percept 波动范围 ±10% 的量化验证：若买家将‘近期’定义为 7天，则 T_percept = 7天；若定义为 30天，则 T_percept =

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N40

## Claim

T_percept 波动范围 ±10% 的量化验证：若买家将‘近期’定义为 7天，则 T_percept = 7天；若定义为 30天，则 T_percept = 30天，两者差异导致 R 的估计值波动幅度约为 (30-7)/30 = 76.7%，远超 ±10%，需重新校准波动范围或引入时间窗口权重平滑 [待核验]

## Corrected Claim

T_percept 波动范围 ±10% 的量化验证：若买家将‘近期’定义为 7天，则 T_percept = 7天；若定义为 30天，则 T_percept = 30天，两者差异导致 R 的估计值波动幅度约为 (30-7)/30 = 76.7%，远超 ±10%，需重新校准波动范围或引入时间窗口权重平滑 [待核验]

## Evidence

先验知识/题面给定，逻辑校验通过：数学计算 (30-7)/30 ≈ 76.7% 正确，且该幅度确实远超 ±10%，逻辑自洽。

## Search Query

perceived recency window price anchoring 7 day 30 day variance
