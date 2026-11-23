# N83: 源站回源命中率 H_origin 受回源带宽限制影响：当回源带宽 B_origin < p_miss * Q_peak * s_avg * 8 时，回源队列延迟

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N25

## Claim

源站回源命中率 H_origin 受回源带宽限制影响：当回源带宽 B_origin < p_miss * Q_peak * s_avg * 8 时，回源队列延迟导致有效命中率下降，修正因子 η = min(1, B_origin / B_required)

## Corrected Claim

源站回源命中率 H_origin 受回源带宽限制影响：当回源带宽 B_origin < p_miss * Q_peak * s_avg * 8 时，回源队列延迟导致有效命中率下降，修正因子 η = min(1, B_origin / B_required)

## Evidence

先验知识/题面给定，逻辑校验通过
