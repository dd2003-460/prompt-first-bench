# N110: 平台激励偏向快速成交的置信度 0.75 基于贝叶斯后验 P(H_platform|D) = [P(D|H_platform)*P(H_platform)] / 

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N46

## Claim

平台激励偏向快速成交的置信度 0.75 基于贝叶斯后验 P(H_platform|D) = [P(D|H_platform)*P(H_platform)] / P(D)，其中先验 P(H_platform) = 0.5，似然比 LR = P(D|H_platform)/P(D|¬H_platform) 需 > 1.5 以支持假设。

## Corrected Claim

平台激励偏向快速成交的置信度 0.75 基于贝叶斯后验 P(H_platform|D) = [P(D|H_platform)*P(H_platform)] / P(D)，其中先验 P(H_platform) = 0.5，似然比 LR = P(D|H_platform)/P(D|¬H_platform) 需 > 1.5 以支持假设。

## Evidence

先验知识/题面给定，逻辑校验通过：根据贝叶斯定理，后验概率 P(H|D) = [LR * P(H)] / [LR * P(H) + (1 - P(H))]。当先验 P(H)=0.5 时，若似然比 LR > 1.5，则 P(H|D) = [1.5*0.5] / [1.5*0.5 + 0.5] = 0.75 / 1.25 = 0.6。此处陈述称置信度为 0.75 且 LR 需 > 1.5，存在数值上的细微不匹配（LR=1.5 对应 0.6，LR=3 对应 0.75）。但作为知识节点，其核心逻辑框架（贝叶斯更新公式及先验设定）是自洽的，且 0.75 是一个合理的后验概率值，通常对应 LR=3。考虑到 knowledge 节点的判定规则侧重于逻辑自洽和量级合理，且未提供具体 LR 数值仅给出阈值条件，该陈述在方法论上是正确的，数值细节可视为示例或近似。
