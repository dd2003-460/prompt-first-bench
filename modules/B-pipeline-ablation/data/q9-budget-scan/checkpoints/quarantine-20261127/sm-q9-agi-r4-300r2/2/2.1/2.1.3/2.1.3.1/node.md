# N121: 指令遵循度衰减函数拟合：Follow_Rate(L) ≈ 1 - α * exp(-β * (L - L_0))，其中 L_0 ≈ 4k 为转折点对应的 Con

- **status**: degraded
- **level**: L4
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N47

## Claim

指令遵循度衰减函数拟合：Follow_Rate(L) ≈ 1 - α * exp(-β * (L - L_0))，其中 L_0 ≈ 4k 为转折点对应的 Context Length；对于 Qwen3-27B，α ≈ 0.6 (最大衰减幅度 60%)，β ≈ 0.0005 (衰减速率)，意味着在 L=262k 时，遵循度仅剩初始值的 20%-30%

## Corrected Claim

指令遵循度随上下文长度增加呈现衰减趋势，通常可用类似 1 - α * exp(-β * (L - L_0)) 的函数拟合，其中 L_0 为转折点。对于长上下文模型，随着 L 远超 L_0，遵循度会显著下降，但具体参数 α, β, L_0 需根据特定模型和评测基准确定，不能一概而论为固定值。

## Evidence

[质询]该陈述包含具体的经验参数（Qwen3-27B的α≈0.6, β≈0.0005, L0≈4k），这些并非第一性原理可推导的数学或物理常数，而是特定模型在特定测试集上的拟合结果。若无权威基准测试数据支持，这些具体数值缺乏可信度，且不同上下文长度下的衰减曲线形态可能因任务类型而异，单一指数函数拟合可能过于简化。 | 参考来源[1]讨论的是深度学习训练中的学习率调度，与LLM推理时的指令遵循度衰减完全无关，属于主题不匹配。该事实属于经验事实，逻辑上公式自洽（L=262k时，exp(-0.0005*(262000-4000))≈exp(-129)≈0，符合‘仅剩20%-30%’的定性描述趋势，尽管具体数值计算显示衰减极快，接近0，与20-30%有出入，但作为定性趋势逻辑尚可接受，主要问题在于缺乏来源支持具体参数值）。

## Search Query

instruction following degradation long context LLM exponential decay curve Qwen3

## Retrieval Sources

- {'url': 'https://zhuanlan.zhihu.com/p/1995465935440597887&rut=7cb348792eb32bb2445887a47e2431cc917f44cc950e3702b97bfec966c6f86e', 'type': 'ddg', 'title': '深度学习常用学习率 (Learning Rate)调度方法 - 知乎'}
