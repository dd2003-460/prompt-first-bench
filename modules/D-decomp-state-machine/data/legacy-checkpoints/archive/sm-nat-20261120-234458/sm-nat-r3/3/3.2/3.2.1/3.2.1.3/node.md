# N153: 折损系数对驻留时间分布的敏感度分析：由于冷对象（低频）驻留时间长（T_res 大），即使其字节占比低，若更新率恒定，冷对象的累积失效概率 P_invalidat

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N48

## Claim

折损系数对驻留时间分布的敏感度分析：由于冷对象（低频）驻留时间长（T_res 大），即使其字节占比低，若更新率恒定，冷对象的累积失效概率 P_invalidate_cold = 1 - exp(-λ_update * T_res_cold) 会高于热对象；需计算冷对象（Bottom 50% 热度）在稳态下的平均驻留时间 T_res_cold 以量化其对 D_bytes 的贡献比例。

## Corrected Claim

折损系数对驻留时间分布的敏感度分析：由于冷对象（低频）驻留时间长（T_res 大），即使其字节占比低，若更新率恒定，冷对象的累积失效概率 P_invalidate_cold = 1 - exp(-λ_update * T_res_cold) 会高于热对象；需计算冷对象（Bottom 50% 热度）在稳态下的平均驻留时间 T_res_cold 以量化其对 D_bytes 的贡献比例。

## Evidence

先验知识/题面给定，逻辑校验通过：基于指数分布失效模型，驻留时间越长累积失效概率越高，冷对象驻留时间长导致其失效概率高于热对象符合逻辑直觉。
