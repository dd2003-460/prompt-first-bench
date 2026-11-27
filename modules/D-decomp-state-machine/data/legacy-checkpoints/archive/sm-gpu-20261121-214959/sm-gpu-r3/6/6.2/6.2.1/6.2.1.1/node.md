# N288: INT4 量化在医疗/法律高风险场景下的具体质量损失量化：基于 N118-N120，INT4 在 MMLU-Pro 下降 2-3% (绝对值)，在 GSM8K 

- **status**: degraded
- **level**: L4
- **source**: search
- **edge_type**: quotient
- **rework_count**: 1
- **parent_ids**: N105

## Claim

INT4 量化在医疗/法律高风险场景下的具体质量损失量化：基于 N118-N120，INT4 在 MMLU-Pro 下降 2-3% (绝对值)，在 GSM8K 下降 5-6%。在医疗问答基准 (如 MedQA) 上，预计准确率下降 3-5% [待核验]，且幻觉率 (Hallucination Rate) 上升 10-15% [待核验]。此风险水平超过医疗/法律场景通常允许的 <1% 误差阈值，故排除 INT4。

## Corrected Claim

INT4 量化在医疗/法律高风险场景下通常会导致显著的质量损失（如准确率下降和幻觉率上升），具体幅度取决于模型和量化算法，但普遍被认为超过此类场景通常允许的 <1% 误差阈值，故在严格合规场景下通常排除 INT4。

## Evidence

[质询]具体数值（MedQA下降3-5%、幻觉率上升10-15%）缺乏直接实验数据支持，属于基于其他基准（MMLU/GSM8K）的推测性外推，不同模型架构和量化方法（如GPTQ vs AWQ）对医疗领域的影响差异巨大，无法一概而论。 | 经验事实，逻辑自洽但缺来源支持（检索无可用来源，且具体量化损失数值属于经验数据，不可由第一性原理严格推出）

## Search Query

Qwen3-27B INT4 AWQ MedQA accuracy drop hallucination rate
