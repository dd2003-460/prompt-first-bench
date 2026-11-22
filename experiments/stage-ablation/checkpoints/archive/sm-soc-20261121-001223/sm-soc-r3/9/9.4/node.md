# N80: 净现值 (NPV) 平衡点的计算公式：NPV = Σ [ (ΔR_platform_t - ΔR_Trust_t) / (1 + r)^t ]，其中 ΔR_Tr

- **status**: pending
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N26

## Claim

净现值 (NPV) 平衡点的计算公式：NPV = Σ [ (ΔR_platform_t - ΔR_Trust_t) / (1 + r)^t ]，其中 ΔR_Trust_t 为第 t 期因留存率提升带来的额外佣金收入，r 为折现率（通常取 10%-15%），平衡点即 NPV = 0 时的时间 T_break_even，需迭代求解 T_break_even。

## Corrected Claim

净现值 (NPV) 平衡点的计算公式：NPV = Σ [ (ΔR_platform_t - ΔR_Trust_t) / (1 + r)^t ]，其中 ΔR_Trust_t 为第 t 期因留存率提升带来的额外佣金收入，r 为折现率（通常取 10%-15%），平衡点即 NPV = 0 时的时间 T_break_even，需迭代求解 T_break_even。

## Evidence

父节点级核验未通过：不完备, 有冗余（子节点本质上是同一公式在不同参数（折现率r和留存增长趋势）下的两个具体算例，存在高度冗余；且仅提供了两个离散案例，未覆盖父节点中定义的通用求解逻辑（如迭代方法）或中间参数区间，导致对父节点“计算公式及求解过程”的覆盖不完备。）

## Search Query

NPV break-even point platform intervention commission loss trust gain
