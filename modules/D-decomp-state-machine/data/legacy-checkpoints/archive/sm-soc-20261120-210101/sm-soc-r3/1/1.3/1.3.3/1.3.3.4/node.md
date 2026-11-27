# N160: 停止阈值 θ_stop 的临界偏离度 D* 推导：令 E[U|stop] = E[U|continue]，解出 D* = (C_search_remaining

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: stochastic
- **rework_count**: 0
- **parent_ids**: N40

## Claim

停止阈值 θ_stop 的临界偏离度 D* 推导：令 E[U|stop] = E[U|continue]，解出 D* = (C_search_remaining(t) - E[V_true|continue]) / (λ_price_penalty * P_ref)。若 E[V_true|continue] 近似为 0（无新信息），则 D* ≈ C_search_remaining(t) / (λ_price_penalty * P_ref)。此公式用于计算买家在特定时间 t 下能容忍的最大溢价。

## Corrected Claim

停止阈值 θ_stop 的临界偏离度 D* 推导：令 E[U|stop] = E[U|continue]，解出 D* = (C_search_remaining(t) - E[V_true|continue]) / (λ_price_penalty * P_ref)。若 E[V_true|continue] 近似为 0（无新信息），则 D* ≈ C_search_remaining(t) / (λ_price_penalty * P_ref)。此公式用于计算买家在特定时间 t 下能容忍的最大溢价。

## Evidence

先验知识/题面给定，逻辑校验通过

## Search Query

satisficing threshold price deviation formula search theory
