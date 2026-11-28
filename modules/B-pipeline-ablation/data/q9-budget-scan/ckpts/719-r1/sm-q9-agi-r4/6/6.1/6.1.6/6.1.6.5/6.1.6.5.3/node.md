# N724: Few-Shot 与 CoT 的叠加效应 (Interaction Effect)：同时使用 Few-Shot (k=3) 和 CoT 提示时，成功率 P_co

- **status**: verified
- **level**: L5
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N265

## Claim

Few-Shot 与 CoT 的叠加效应 (Interaction Effect)：同时使用 Few-Shot (k=3) 和 CoT 提示时，成功率 P_combined 是否等于 P_zs + Delta_cot + Delta_fs？定义交互项 I = P_combined - (P_zs + Delta_cot + Delta_fs)，若 I < 0 表明存在提示冲突，需量化冲突导致的性能损失百分比

## Corrected Claim

Few-Shot 与 CoT 的叠加效应 (Interaction Effect)：同时使用 Few-Shot (k=3) 和 CoT 提示时，成功率 P_combined 是否等于 P_zs + Delta_cot + Delta_fs？定义交互项 I = P_combined - (P_zs + Delta_cot + Delta_fs)，若 I < 0 表明存在提示冲突，需量化冲突导致的性能损失百分比

## Evidence

先验知识/题面给定，逻辑校验通过：该陈述定义了Few-Shot与CoT叠加效应的交互项I及其符号含义（I<0表示冲突），符合实验设计中的主效应与交互效应分解逻辑，量纲与定义自洽。

## Search Query

interaction effect few-shot and chain-of-thought prompting LLM
