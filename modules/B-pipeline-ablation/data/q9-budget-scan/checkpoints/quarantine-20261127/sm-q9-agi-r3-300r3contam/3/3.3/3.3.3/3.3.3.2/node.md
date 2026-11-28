# N157: 冷门领域（如量子引力、古生物分类学）的知识覆盖率 C_cold 显著降低，估计 C_cold ≈ 0.4-0.6，导致 P_offline_cold ≈ 0.4

- **status**: degraded
- **level**: L4
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 1
- **parent_ids**: N61

## Claim

冷门领域（如量子引力、古生物分类学）的知识覆盖率 C_cold 显著降低，估计 C_cold ≈ 0.4-0.6，导致 P_offline_cold ≈ 0.4-0.6；此时必须依赖外部检索，纯离线模式无法满足 <5% 虚构率要求，需切换至在线混合模式

## Corrected Claim

冷门领域（如量子引力、古生物分类学）的知识覆盖率 C_cold 通常显著低于热门领域，导致纯离线模式的虚构率往往难以满足 <5% 的高标准要求，因此在此类场景下通常需要依赖外部检索或切换至在线混合模式以提升准确性。

## Evidence

[质询]数值量级缺乏实证支撑：C_cold ≈ 0.4-0.6 是一个具体的经验估计值，不同模型架构、训练数据分布及评估基准下，冷门领域的知识覆盖率波动极大，该区间可能过于乐观或悲观，且‘显著降低’的具体阈值定义模糊。 | 逻辑自洽：冷门领域知识稀疏导致离线生成幻觉率上升，进而需要外部检索辅助以降低虚构率，符合大模型能力边界的基本直觉；但作为 knowledge 节点，虽逻辑通顺，具体数值区间（0.4-0.6）属于经验性估计，缺乏通用共识或第一性原理严格推导，故降级为定性表述。

## Search Query

LLM long-tail knowledge coverage niche domain citation hallucination rate estimation
