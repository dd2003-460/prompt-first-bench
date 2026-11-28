# N201: Lost in the Middle 效应的量化边界：在 RoPE 位置编码下，当查询位置 Q_pos 远离上下文中心 C_pos 时，注意力权重衰减系数 α 

- **status**: degraded
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N78

## Claim

Lost in the Middle 效应的量化边界：在 RoPE 位置编码下，当查询位置 Q_pos 远离上下文中心 C_pos 时，注意力权重衰减系数 α = exp(-λ * |Q_pos - C_pos| / max_len)，其中 λ≈0.001 [待核验]；Map-Territory 策略通过将关键信息聚合至 Map（位置 0-2k），使有效距离缩短，从而将 α 提升至 >0.8，确保召回率不随原文长度线性下降

## Corrected Claim

在RoPE位置编码下，注意力权重通常随查询位置与上下文中心距离的增加而衰减。Map-Territory策略通过将关键信息聚合至靠近起始位置（如位置0-2k），缩短了有效距离，从而增强了对关键信息的注意力权重，有助于缓解长文本中关键信息召回率下降的问题。

## Evidence

[质询]该陈述包含具体的经验参数（λ≈0.001）和特定的量化阈值（α>0.8），这些并非RoPE位置编码的第一性原理推导结果，而是依赖于具体模型架构、训练数据及实验条件的经验观测值。此外，'Lost in the Middle'效应通常被描述为U型注意力分布，而非简单的指数衰减函数，且Map-Territory策略的具体实现细节和效果量化缺乏通用标准定义。 | source=knowledge，逻辑自洽（距离越近注意力越强符合直觉），但λ值和α阈值属于特定实验下的经验事实，非普适物理/数学定律，且无外部来源支持具体数值，故降级。

## Search Query

RoPE attention decay factor long context lost in the middle quantitative analysis
