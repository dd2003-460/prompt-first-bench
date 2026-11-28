# N81: 冲突检测需区分‘直接矛盾’与‘间接不一致’：直接矛盾定义为生成结论与检索文献结论的逻辑否定（Negation），通过 LLM 判断 Contradiction 

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N26

## Claim

冲突检测需区分‘直接矛盾’与‘间接不一致’：直接矛盾定义为生成结论与检索文献结论的逻辑否定（Negation），通过 LLM 判断 Contradiction Label = True/False；间接不一致定义为数值偏差 > 10% 或方向相反，需计算相对误差 RE = |gen_val - lit_val| / lit_val，RE > 0.1 触发警报。

## Corrected Claim

冲突检测需区分‘直接矛盾’与‘间接不一致’：直接矛盾定义为生成结论与检索文献结论的逻辑否定（Negation），通过 LLM 判断 Contradiction Label = True/False；间接不一致定义为数值偏差 > 10% 或方向相反，需计算相对误差 RE = |gen_val - lit_val| / lit_val，RE > 0.1 触发警报。

## Evidence

先验知识/题面给定，逻辑校验通过

## Search Query

fact contradiction detection relative error threshold scientific literature comparison
