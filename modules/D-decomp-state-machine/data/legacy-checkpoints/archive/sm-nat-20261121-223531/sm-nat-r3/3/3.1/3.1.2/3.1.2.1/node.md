# N137: 在1%/天更新率下，LRU中对象因更新而逻辑失效（stale）的有效容量折损因子 D_stale = 1 - e^{-λ_upd * T_res_avg}，其中

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N48

## Claim

在1%/天更新率下，LRU中对象因更新而逻辑失效（stale）的有效容量折损因子 D_stale = 1 - e^{-λ_upd * T_res_avg}，其中 T_res_avg 为对象平均驻留时间。对于热门对象（前1%），T_res ≈ 86.4s，D_stale ≈ 0.00001，几乎无影响；对于冷门对象（后90%），T_res ≈ 0，D_stale ≈ 0，但需考虑重新缓存延迟。

## Corrected Claim

在1%/天更新率下，LRU中对象因更新而逻辑失效（stale）的有效容量折损因子 D_stale = 1 - e^{-λ_upd * T_res_avg}，其中 T_res_avg 为对象平均驻留时间。对于热门对象（前1%），T_res ≈ 86.4s，D_stale ≈ 0.00001，几乎无影响；对于冷门对象（后90%），T_res ≈ 0，D_stale ≈ 0，但需考虑重新缓存延迟。

## Evidence

先验知识/题面给定，逻辑校验通过：公式 D_stale = 1 - e^{-λT} 符合指数衰减模型，数值量级（λ=1/86400, T=86.4 -> D≈1e-5）计算正确，逻辑自洽。
