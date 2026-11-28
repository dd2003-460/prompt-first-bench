# N338: 基于修正后的成本比（3750x）和错误率（0.25 vs 0.01），高风险任务的最优抽查率 r_High* 应趋近于 100%（全检），因为漏检一次的期望损失

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N107

## Claim

基于修正后的成本比（3750x）和错误率（0.25 vs 0.01），高风险任务的最优抽查率 r_High* 应趋近于 100%（全检），因为漏检一次的期望损失（$37.5 × 0.25）远大于全检的人工成本分摊；低风险任务 r_Low* 可通过最小化 E[C] 求解，若 C_Human 固定，r_Low* 应低于 5% 以平衡漏检风险与人工开销

## Corrected Claim

基于修正后的成本比（3750x）和错误率（0.25 vs 0.01），高风险任务的最优抽查率 r_High* 应趋近于 100%（全检），因为漏检一次的期望损失（$37.5 × 0.25）远大于全检的人工成本分摊；低风险任务 r_Low* 可通过最小化 E[C] 求解，若 C_Human 固定，r_Low* 应低于 5% 以平衡漏检风险与人工开销

## Evidence

先验知识/题面给定，逻辑校验通过：高错误率(0.25)与高单次损失($37.5)导致漏检期望成本极高，全检(r=100%)符合最优决策逻辑；低错误率(0.01)下，边际漏检成本远低于边际人工成本，故最优抽查率极低(<5%)，推导自洽。

## Search Query

optimal sampling rate cost-benefit analysis quality control
