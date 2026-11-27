# N208: 初始搜寻成本 Initial_BS 的基准定义：Initial_BS = N_old * k_search + (P_ask - R_true)_baselin

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N72

## Claim

初始搜寻成本 Initial_BS 的基准定义：Initial_BS = N_old * k_search + (P_ask - R_true)_baseline。其中 R_true 为买家真实保留价，(P_ask - R_true)_baseline 代表在无信息展示时，买家为避免买贵而预留的心理安全边际成本，通常假设为价格波动的 1 个标准差 (0.18 * P_market)。

## Corrected Claim

初始搜寻成本 Initial_BS 的基准定义：Initial_BS = N_old * k_search + (P_ask - R_true)_baseline。其中 R_true 为买家真实保留价，(P_ask - R_true)_baseline 代表在无信息展示时，买家为避免买贵而预留的心理安全边际成本，通常假设为价格波动的 1 个标准差 (0.18 * P_market)。

## Evidence

先验知识/题面给定，逻辑校验通过
