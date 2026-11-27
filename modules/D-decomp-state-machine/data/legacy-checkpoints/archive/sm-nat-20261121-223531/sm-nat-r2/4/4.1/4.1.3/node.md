# N54: 热门对象（前1%）的更新折损因子 D_hot = 1 - e^{-λ_upd * T_res_hot}，其中 T_res_hot ≈ 86.4s（基于前1%对象

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N16

## Claim

热门对象（前1%）的更新折损因子 D_hot = 1 - e^{-λ_upd * T_res_hot}，其中 T_res_hot ≈ 86.4s（基于前1%对象接收请求频率），λ_upd=1%/天，计算得 D_hot ≈ 1 - e^{-0.01 * 86.4/86400} ≈ 1 - e^{-0.00001} ≈ 0.00001，即热门对象折损可忽略。

## Corrected Claim

热门对象（前1%）的更新折损因子 D_hot = 1 - e^{-λ_upd * T_res_hot}，其中 T_res_hot ≈ 86.4s（基于前1%对象接收请求频率），λ_upd=1%/天，计算得 D_hot ≈ 1 - e^{-0.01 * 86.4/86400} ≈ 1 - e^{-0.00001} ≈ 0.00001，即热门对象折损可忽略。

## Evidence

先验知识/题面给定，逻辑校验通过：数学计算 1 - e^{-0.00001} ≈ 0.00001 正确，量级合理，符合指数衰减近似原理。

## Search Query

hot object update penalty LRU cache residence time
