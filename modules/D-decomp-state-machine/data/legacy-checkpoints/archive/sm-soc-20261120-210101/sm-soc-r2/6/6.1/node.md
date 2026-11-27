# N103: E_high 的基准参照系 P_ref 必须明确为'近7天同类商品加权成交均价'，权重 w_i 按成交量或时间衰减 λ_t 计算，公式为 P_ref = Σ(P

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N27, N28, N29

## Claim

E_high 的基准参照系 P_ref 必须明确为'近7天同类商品加权成交均价'，权重 w_i 按成交量或时间衰减 λ_t 计算，公式为 P_ref = Σ(P_i * w_i) / Σ(w_i)，其中 w_i = exp(-λ_t * (t_now - t_i))，λ_t 取值为 0.1/day。

## Corrected Claim

E_high 的基准参照系 P_ref 必须明确为'近7天同类商品加权成交均价'，权重 w_i 按成交量或时间衰减 λ_t 计算，公式为 P_ref = Σ(P_i * w_i) / Σ(w_i)，其中 w_i = exp(-λ_t * (t_now - t_i))，λ_t 取值为 0.1/day。

## Evidence

先验知识/题面给定，逻辑校验通过

## Search Query

weighted average price time decay lambda 0.1 per day
