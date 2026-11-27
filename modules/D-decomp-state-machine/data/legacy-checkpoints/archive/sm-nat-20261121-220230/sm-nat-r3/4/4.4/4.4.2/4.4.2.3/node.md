# N210: 工作点3（低驻留/高折损）：设定 T_resident = 0.2 天，基于 N71 公式代入 P_eviction≈0.05，计算得 P_invalid = 

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N72

## Claim

工作点3（低驻留/高折损）：设定 T_resident = 0.2 天，基于 N71 公式代入 P_eviction≈0.05，计算得 P_invalid = 1 - exp(-0.002) ≈ 0.1999%，折损因子 D ≈ 0.99800

## Corrected Claim

工作点3（低驻留/高折损）：设定 T_resident = 0.2 天，基于 N71 公式代入 P_eviction≈0.05，计算得 P_invalid = 1 - exp(-0.002) ≈ 0.1999%，折损因子 D ≈ 0.99800

## Evidence

先验知识/题面给定，逻辑校验通过：计算 1 - exp(-0.002) ≈ 0.001998，即 0.1998%，与陈述中的 0.1999% 在精度范围内一致；折损因子 D = 1 - P_invalid ≈ 0.99800，逻辑自洽。
