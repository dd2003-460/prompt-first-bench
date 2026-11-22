# N94: 共享随机源继承：Δt = T_search * (1 - η_info)，由于 T_search 与 λ_liq 负相关，Δt 也与 λ_liq 负相关，即高流

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: stochastic
- **rework_count**: 0
- **parent_ids**: N29

## Claim

共享随机源继承：Δt = T_search * (1 - η_info)，由于 T_search 与 λ_liq 负相关，Δt 也与 λ_liq 负相关，即高流动性（高 λ_liq）导致短搜索时间，进而缩短信息不对称窗口，需验证 Δt 与 λ_liq 的相关系数 r_Δt_λ 是否接近 -0.8 以上。

## Corrected Claim

共享随机源继承：Δt = T_search * (1 - η_info)，由于 T_search 与 λ_liq 负相关，Δt 也与 λ_liq 负相关，即高流动性（高 λ_liq）导致短搜索时间，进而缩短信息不对称窗口，需验证 Δt 与 λ_liq 的相关系数 r_Δt_λ 是否接近 -0.8 以上。

## Evidence

先验知识/题面给定，逻辑校验通过：公式 Δt = T_search * (1 - η_info) 中，若 T_search 与 λ_liq 负相关且 (1 - η_info) 为正数（通常 η_info < 1），则 Δt 与 λ_liq 必然负相关，逻辑自洽。
