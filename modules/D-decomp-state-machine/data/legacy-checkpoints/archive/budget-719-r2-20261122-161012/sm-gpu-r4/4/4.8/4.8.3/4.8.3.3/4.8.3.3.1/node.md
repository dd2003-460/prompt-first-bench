# N640: 创意写作场景下的质量损失阈值修正：若应用场景为创意写作，MMLU 阈值放宽至 <3% 的同时，需引入 BLEU-4 或 ROUGE-L 分数作为辅助指标；INT

- **status**: degraded
- **level**: L5
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N264

## Claim

创意写作场景下的质量损失阈值修正：若应用场景为创意写作，MMLU 阈值放宽至 <3% 的同时，需引入 BLEU-4 或 ROUGE-L 分数作为辅助指标；INT4 量化在创意写作任务中的 BLEU-4 下降通常控制在 <5% 以内，若满足此条件，即使 MMLU 下降 3%，INT4 方案仍可判定为可行。

## Corrected Claim

在创意写作场景下，若MMLU下降控制在较小范围（如<3%），且BLEU-4或ROUGE-L分数下降在可接受范围内（如<5%），INT4量化方案通常被视为可行，但具体阈值需根据实际业务容忍度调整。

## Evidence

[质询]该陈述包含具体的经验性阈值（MMLU <3%, BLEU-4 <5%），这些数值并非从第一性原理或数学公理严格推导出的必然结论，而是基于特定实验或行业惯例的经验设定，缺乏普适的理论推导基础。 | 逻辑自洽，但属于经验事实（具体量化阈值），且无外部来源支持，依据经验事实排除条款降级。

## Search Query

creative writing LLM evaluation BLEU ROUGE quantization impact
