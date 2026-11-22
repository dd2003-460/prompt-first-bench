# N63: 基准值 P_rec 的估计误差 σ_rec 的量化：P_rec = Σ P_deal_j * w_j，其中 w_j 为第 j 笔交易的时间衰减权重（w_j = 

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N23

## Claim

基准值 P_rec 的估计误差 σ_rec 的量化：P_rec = Σ P_deal_j * w_j，其中 w_j 为第 j 笔交易的时间衰减权重（w_j = e^(-λ_t * t_j)），σ_rec = √(Σ (w_j * P_deal_j)^2 * σ_j^2 / (Σ w_j)^2)，该误差需叠加到 P_ask 的总方差中。

## Corrected Claim

基准值 P_rec 的估计误差 σ_rec 的量化：P_rec = Σ P_deal_j * w_j，其中 w_j 为第 j 笔交易的时间衰减权重（w_j = e^(-λ_t * t_j)），σ_rec = √(Σ (w_j * P_deal_j)^2 * σ_j^2 / (Σ w_j)^2)，该误差需叠加到 P_ask 的总方差中。

## Evidence

先验知识/题面给定，逻辑校验通过
