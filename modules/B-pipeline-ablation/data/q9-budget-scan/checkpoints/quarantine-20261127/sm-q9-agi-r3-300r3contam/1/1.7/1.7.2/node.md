# N49: 主题偏离度的量化公式：Deviation = 1 - CosineSim(E_model_output, E_topic_anchor)，其中 E 为 Sent

- **status**: pending
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N13, N14, N19

## Claim

主题偏离度的量化公式：Deviation = 1 - CosineSim(E_model_output, E_topic_anchor)，其中 E 为 Sentence-BERT 嵌入，阈值 δ=0.2 需根据 Top-10% 历史错误样本的 Deviation 分布 P90 值动态调整。

## Corrected Claim

主题偏离度的量化公式：Deviation = 1 - CosineSim(E_model_output, E_topic_anchor)，其中 E 为 Sentence-BERT 嵌入，阈值 δ=0.2 需根据 Top-10% 历史错误样本的 Deviation 分布 P90 值动态调整。

## Evidence

父节点级核验未通过：不完备（子节点在逻辑上是正交的，分别涵盖了输入数据（Embedding）、参考基准（Anchor）、阈值机制和数值稳定性。然而，完备性存在缺失：父节点明确提到了‘根据Top-10%历史错误样本’，但子节点3中定义的N=100是固定窗口，未明确说明如何筛选‘Top-10%’这一特定子集，导致与父节点定义的逻辑链条不完整。此外，父节点提到的‘动态调整’机制在子节点3中仅给出了静态计算公式，未解释随着时间推移或新数据加入时的更新策略（如滑动窗口或加权），略显单薄。）

## Search Query

semantic drift detection cosine similarity threshold sentence-bert
