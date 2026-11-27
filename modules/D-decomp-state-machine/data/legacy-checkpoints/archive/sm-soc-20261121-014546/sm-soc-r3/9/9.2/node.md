# N121: 当前观测“周期变短”的量化约束：成交周期 T 与 σ_buyer 的关系为 T = T_0 * (1 + k * σ_buyer^2)，其中 T_0 为基准周期

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N32

## Claim

当前观测“周期变短”的量化约束：成交周期 T 与 σ_buyer 的关系为 T = T_0 * (1 + k * σ_buyer^2)，其中 T_0 为基准周期，k 为市场敏感度系数，σ_buyer < 0.15 时 T 低于 T_0。

## Corrected Claim

在特定市场模型中，若市场敏感度系数 k 为负值，则成交周期 T 与买方波动率 σ_buyer 的关系为 T = T_0 * (1 + k * σ_buyer^2)，此时当 σ_buyer 较小时 T 可能低于基准周期 T_0；但在常规摩擦成本模型中，k 通常为正值，波动率增加会导致成交周期延长。

## Evidence

父节点级核验通过：正交+完备+无冗余（三个子节点分别独立定义了公式中的三个核心参数（T_0, k, σ_buyer）的量化来源、符号意义及分解结构，彼此之间无逻辑重叠或矛盾。子节点完整覆盖了父节点公式中所有未定义变量的约束条件，且每个子节点代表独立的参数维度，不存在冗余。）

## Search Query

transaction time buyer noise relationship market sensitivity
