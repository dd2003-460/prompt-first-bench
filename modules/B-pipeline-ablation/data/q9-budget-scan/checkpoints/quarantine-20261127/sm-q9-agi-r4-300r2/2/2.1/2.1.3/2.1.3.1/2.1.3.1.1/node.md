# N299: 参数 α (最大衰减幅度) 的物理意义为系统提示词在长上下文下的“遗忘率”，其数值 α=0.6 需通过构建不同长度 (4k-262k) 的 IFEval 基准集

- **status**: degraded
- **level**: L5
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N121

## Claim

参数 α (最大衰减幅度) 的物理意义为系统提示词在长上下文下的“遗忘率”，其数值 α=0.6 需通过构建不同长度 (4k-262k) 的 IFEval 基准集进行回归拟合验证；若实测 α > 0.8，则表明模型对核心指令的鲁棒性不足，需引入指令重述机制。

## Corrected Claim

参数 α 通常被定义为系统提示词在长上下文下的衰减系数，其具体数值（如 0.6）及鲁棒性阈值（如 0.8）需根据特定模型在 IFEval 等基准上的实测回归结果确定，而非固定常数。

## Evidence

[质询]该陈述包含具体的经验参数（α=0.6）和特定的工程阈值（α>0.8），这些并非从第一性原理或数学公理中严格推导出的必然结论，而是依赖于特定模型架构、训练数据分布及评估基准的经验性设定。缺乏通用理论证明表明所有系统在长上下文下必须遵循此特定衰减系数或阈值。 | 先验知识/题面给定，逻辑校验通过；但作为经验事实，缺乏外部来源直接支持具体数值，故降级。

## Search Query

Qwen3 instruction following degradation long context IFEval benchmark alpha parameter
