# N288: 曝光权重惩罚的非线性截断效应：当 W_post 降至阈值 W_min（如基础权重的 50%）以下时，曝光不再线性下降，而是进入‘长尾冻结’状态，此时 ∂T/∂δ

- **status**: degraded
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N80

## Claim

曝光权重惩罚的非线性截断效应：当 W_post 降至阈值 W_min（如基础权重的 50%）以下时，曝光不再线性下降，而是进入‘长尾冻结’状态，此时 ∂T/∂δ_tag 趋于无穷大或发生阶跃式跳变，需引入 Heaviside 阶跃函数修正模型：W_effective = max(W_post, W_min)。

## Corrected Claim

在采用截断机制的曝光权重模型中，当 W_post 降至阈值 W_min 以下时，有效权重被固定为 W_min（即 W_effective = max(W_post, W_min)），导致曝光量不再随惩罚系数线性下降，而是进入饱和或冻结状态。

## Evidence

[质询]该陈述将‘曝光权重惩罚’描述为具有特定数学性质（如导数趋于无穷大、Heaviside阶跃修正）的通用物理/经济规律，但这并非公认的第一性原理或标准数学定义，而是特定算法模型（如推荐系统中的截断机制）的工程实现细节。将其表述为普遍存在的‘非线性截断效应’且伴随‘长尾冻结’等特定术语，缺乏通用理论支持，属于特定场景下的经验性建模假设，而非普适事实。 | 先验知识/题面给定，逻辑校验通过（max函数确实导致导数在阈值处不连续或为0/无穷，符合数学逻辑），但作为通用事实陈述缺乏来源支持且属于特定工程经验，故降级。

## Search Query

algorithmic listing visibility floor threshold marketplace long tail
