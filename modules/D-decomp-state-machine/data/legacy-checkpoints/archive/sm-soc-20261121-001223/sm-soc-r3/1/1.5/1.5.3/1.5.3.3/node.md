# N125: 工作点 C（低转化/长周期）：当高挂价触发‘捡漏’心理但导致买家犹豫，使 k_deal 降至基准区间下界 0.3，且 k_consult 仅微幅提升（1.1 *

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N44

## Claim

工作点 C（低转化/长周期）：当高挂价触发‘捡漏’心理但导致买家犹豫，使 k_deal 降至基准区间下界 0.3，且 k_consult 仅微幅提升（1.1 * k_consult_base）时，成交周期 T_deal 反而长于基准周期，量化了‘高溢价导致决策摩擦’的负面边界。

## Corrected Claim

工作点 C（低转化/长周期）：当高挂价触发‘捡漏’心理但导致买家犹豫，使 k_deal 降至基准区间下界 0.3，且 k_consult 仅微幅提升（1.1 * k_consult_base）时，成交周期 T_deal 反而长于基准周期，量化了‘高溢价导致决策摩擦’的负面边界。

## Evidence

先验知识/题面给定，逻辑校验通过：在交易模型中，成交周期通常与成交概率（k_deal）成反比，k_deal 降至下界 0.3 必然导致 T_deal 显著延长，符合经济直觉与逻辑自洽。
