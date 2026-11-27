# N139: LRU 稳态下对象被驱逐的最近访问时间阈值 T_threshold_l 的解析估算：基于 Little's Law，λ = C / (R_total * E[S

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N51

## Claim

LRU 稳态下对象被驱逐的最近访问时间阈值 T_threshold_l 的解析估算：基于 Little's Law，λ = C / (R_total * E[S_miss])，T_threshold_l ≈ λ。若 λ ≈ 1.18 天（基于 H_base=0.78），则 T_threshold_l ≈ 1.18 天。

## Corrected Claim

LRU 稳态下对象被驱逐的最近访问时间阈值 T_threshold_l 的解析估算：基于 Little's Law，λ = C / (R_total * E[S_miss])，T_threshold_l ≈ λ。若 λ ≈ 1.18 天（基于 H_base=0.78），则 T_threshold_l ≈ 1.18 天。

## Evidence

先验知识/题面给定，逻辑校验通过：基于Little's Law推导LRU驱逐阈值在量纲和逻辑上自洽，数值量级合理。
