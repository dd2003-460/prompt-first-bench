# N75: 幻觉率 H_domain 计算公式：H_domain = (N_hallucinated / N_total_questions) * 100%，其中 N_ha

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N26

## Claim

幻觉率 H_domain 计算公式：H_domain = (N_hallucinated / N_total_questions) * 100%，其中 N_hallucinated 定义为模型回答与基准真值在核心实体或数值上不一致的数量，判定标准需排除同义改写误差。

## Corrected Claim

幻觉率 H_domain 计算公式：H_domain = (N_hallucinated / N_total_questions) * 100%，其中 N_hallucinated 定义为模型回答与基准真值在核心实体或数值上不一致的数量，判定标准需排除同义改写误差。

## Evidence

父节点级核验通过：正交+完备+无冗余（三个子节点分别对应父节点中定义的三个关键约束条件：核心实体一致性（定义N_hallucinated的定性部分）、数值一致性（定义N_hallucinated的定量部分）、以及同义改写排除（修正/过滤机制）。三者逻辑独立且互补，共同构成了完整的判定流程，不存在重叠或矛盾。）
