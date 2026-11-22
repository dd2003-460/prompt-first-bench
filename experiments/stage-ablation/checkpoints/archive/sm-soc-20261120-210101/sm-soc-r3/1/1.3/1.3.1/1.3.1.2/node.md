# N151: 下游投影1（短期搜索者）：当买家搜索历史长度 L_search 较短（L_search < 5次点击）时，信息积累不足，不确定性高。假设 σ_buyer = 0

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N38

## Claim

下游投影1（短期搜索者）：当买家搜索历史长度 L_search 较短（L_search < 5次点击）时，信息积累不足，不确定性高。假设 σ_buyer = 0.3 * P_ref。此时 ε_buyer 的分布较宽，导致买家更容易因随机扰动而停止搜索（‘过早放弃’）或继续搜索（‘过度搜索’），是造成‘48小时无咨询’随机波动的主要来源。

## Corrected Claim

下游投影1（短期搜索者）：当买家搜索历史长度 L_search 较短（L_search < 5次点击）时，信息积累不足，不确定性高。假设 σ_buyer = 0.3 * P_ref。此时 ε_buyer 的分布较宽，导致买家更容易因随机扰动而停止搜索（‘过早放弃’）或继续搜索（‘过度搜索’），是造成‘48小时无咨询’随机波动的主要来源。

## Evidence

先验知识/题面给定，逻辑校验通过：搜索历史短导致信息熵高、不确定性大，进而增加决策随机性，符合信息经济学与搜索理论的基本逻辑。

## Search Query

short search history buyer decision variance
