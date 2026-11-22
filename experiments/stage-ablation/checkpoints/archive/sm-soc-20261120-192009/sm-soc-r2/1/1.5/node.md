# N9: 信息摩擦导致的信号更新：平台算法或社交传播使 info_quality 随时间 t 增加，info_quality(t) = info_0 + γ * t；当 

- **status**: verified
- **level**: L2
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N1

## Claim

信息摩擦导致的信号更新：平台算法或社交传播使 info_quality 随时间 t 增加，info_quality(t) = info_0 + γ * t；当 info_quality 超过阈值 θ_verify 时，买家能识别‘虚高’，导致有效需求集中在真实价值附近，从而缩短成交周期（因为筛选掉了无效咨询）。

## Corrected Claim

信息摩擦导致的信号更新：平台算法或社交传播使 info_quality 随时间 t 增加，info_quality(t) = info_0 + γ * t；当 info_quality 超过阈值 θ_verify 时，买家能识别‘虚高’，导致有效需求集中在真实价值附近，从而缩短成交周期（因为筛选掉了无效咨询）。

## Evidence

父节点级核验通过：正交+完备+无冗余（子节点分别对应父节点模型中的随机源（ε_network）、核心参数量化（γ）、阈值分布（θ_verify）以及结果机制（成交周期/有效咨询率）。四个维度（随机性、输入参数、触发条件、输出效应）互不重叠且逻辑独立，共同构成了完整的因果链条，未发现冗余或矛盾。）
