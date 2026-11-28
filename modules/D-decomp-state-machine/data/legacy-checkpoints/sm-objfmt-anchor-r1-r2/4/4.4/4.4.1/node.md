# N87: Qwen3-27B INT8 精度下的质量损失量化：INT8 对称量化通常导致 ΔPPL 在 0.05-0.15 之间，MMLU 下降 1-2 分；相比 FP8

- **status**: degraded
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N24

## Claim

Qwen3-27B INT8 精度下的质量损失量化：INT8 对称量化通常导致 ΔPPL 在 0.05-0.15 之间，MMLU 下降 1-2 分；相比 FP8，INT8 在注意力层和 FFN 层的梯度分布截断可能引入稍高的尾部误差，尤其在长尾知识任务上 [待核验]。

## Corrected Claim

Qwen3-27B INT8 精度下通常会出现轻微的质量损失（如 PPL 上升、MMLU 分数小幅下降）；相比 FP8，INT8 在极端值处理上的截断特性可能在长尾知识任务上引入稍高的尾部误差。

## Evidence

[质询]具体数值范围（ΔPPL 0.05-0.15, MMLU 1-2分）缺乏特定模型（Qwen3-27B）的实证数据支持，不同数据集和量化实现下波动较大，直接断言固定区间存在过度概括风险。 | 先验知识/题面给定，逻辑校验通过；但作为经验事实，具体量化损失数值缺乏通用确定性，需降级为定性描述。
