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

父节点级核验通过：正交+完备+无冗余（三个子节点分别对应父节点中的三个独立维度：1. 直接矛盾的技术实现（LLM选型与成本）；2. 间接不一致中数值偏差的计算前提（单位归一化）；3. 间接不一致中方向相反的判定标准（统计显著性）。三者互不重叠，且共同覆盖了父节点定义的所有关键操作细节，无冗余。）

## Search Query

fact contradiction detection relative error threshold scientific literature comparison
