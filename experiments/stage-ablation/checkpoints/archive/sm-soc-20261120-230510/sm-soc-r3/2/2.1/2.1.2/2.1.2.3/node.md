# N152: 推荐权重 W 对 G 的非线性影响：若排序算法采用加权线性模型 Score = w_ctr*CTR + w_cvr*CVR，则 W 的变化不仅影响 Q_expo

- **status**: degraded
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N45

## Claim

推荐权重 W 对 G 的非线性影响：若排序算法采用加权线性模型 Score = w_ctr*CTR + w_cvr*CVR，则 W 的变化不仅影响 Q_exposure，还可能通过改变竞争环境间接影响 CTR/CVR；需量化 W 从 1.0 降至 0.5 时，G 的总变化率 ∂ln(G)/∂ln(W)，典型值 ∈ [-1.2, -0.8]。

## Corrected Claim

推荐权重 W 对 G 的非线性影响：若排序算法采用加权线性模型 Score = w_ctr*CTR + w_cvr*CVR，则 W 的变化不仅影响 Q_exposure，还可能通过改变竞争环境间接影响 CTR/CVR；需量化 W 从 1.0 降至 0.5 时，G 的总变化率 ∂ln(G)/∂ln(W)，该值通常为负，具体数值取决于业务场景及竞争动态。

## Evidence

[质询]该陈述将复杂的系统动力学效应（竞争环境改变导致的CTR/CVR间接变化）简化为一个固定的典型数值区间[-1.2, -0.8]，缺乏具体的业务场景、数据分布或模型假设支撑，属于过度简化的经验断言，且“典型值”的定义模糊。 | 先验知识/题面给定，逻辑校验通过：加权线性模型中权重降低确实会减少曝光量（Q_exposure），且可能通过改变竞争格局影响点击/转化率，导致总收益G下降，弹性系数为负符合直觉；但具体数值区间[-1.2, -0.8]属于经验估计，无来源支持，故降级。
