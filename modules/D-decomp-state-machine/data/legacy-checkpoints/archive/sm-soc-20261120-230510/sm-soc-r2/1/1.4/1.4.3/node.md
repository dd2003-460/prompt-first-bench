# N43: 成交时间函数：T_deal = g(μ_U_resid, S, C_wait)，其中 C_wait 为买家等待成本；由于剩余买家 μ_U_resid 更高且 S

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: stochastic
- **rework_count**: 0
- **parent_ids**: N9

## Claim

成交时间函数：T_deal = g(μ_U_resid, S, C_wait)，其中 C_wait 为买家等待成本；由于剩余买家 μ_U_resid 更高且 S 更高（竞争更少），g 对 S 的偏导数 ∂T_deal/∂S < 0，导致 T_deal 随筛选强度增加而缩短。

## Corrected Claim

成交时间函数：T_deal = g(μ_U_resid, S, C_wait)，其中 C_wait 为买家等待成本；由于剩余买家 μ_U_resid 更高且 S 更高（竞争更少），g 对 S 的偏导数 ∂T_deal/∂S < 0，导致 T_deal 随筛选强度增加而缩短。

## Evidence

先验知识/题面给定，逻辑校验通过：在匹配理论中，供给方（卖家）数量S增加通常降低买方搜索/等待成本，从而缩短成交时间，符合经济学直觉。
