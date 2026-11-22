# N74: W4 量化的可接受性阈值定义：若下游任务为代码生成，Pass@1 相对损失 > 10% 视为不可接受；若为通用对话，PPL 相对增加 > 15% 视为不可接受。

- **status**: degraded
- **level**: L3
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 1
- **parent_ids**: N19

## Claim

W4 量化的可接受性阈值定义：若下游任务为代码生成，Pass@1 相对损失 > 10% 视为不可接受；若为通用对话，PPL 相对增加 > 15% 视为不可接受。Qwen3-27B W4 在此阈值下的判定为 [待核验]。

## Corrected Claim

W4 量化的可接受性阈值定义（示例）：若下游任务为代码生成，Pass@1 相对损失 > 10% 视为不可接受；若为通用对话，PPL 相对增加 > 15% 视为不可接受。Qwen3-27B W4 在此阈值下的判定为 [待核验]。

## Evidence

[质询]阈值定义（Pass@1 > 10%, PPL > 15%）属于特定研究或工程实践中的经验性标准，并非通用的第一性原理或数学公理，且不同文献/场景下对'可接受'的定义可能存在差异，缺乏普适性依据。 | source=knowledge，逻辑自洽（阈值定义在量纲和数值量级上合理），但作为经验性标准，缺乏外部来源直接支持其普适性或特定上下文下的唯一性，依据经验事实排除条款及knowledge节点在存在可信攻击点时的降档规则，判定为degraded。

## Search Query

LLM quantization quality acceptance threshold pass@1 ppl relative loss
