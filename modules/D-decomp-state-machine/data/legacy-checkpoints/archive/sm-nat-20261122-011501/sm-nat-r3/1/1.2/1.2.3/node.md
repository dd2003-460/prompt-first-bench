# N30: 热度分布的截断修正：由于 N 有限，Pareto 分布需在 h_min 处截断。h_min = h_max * (N / N_hot)^(1/0.9)，其中 N

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N7

## Claim

热度分布的截断修正：由于 N 有限，Pareto 分布需在 h_min 处截断。h_min = h_max * (N / N_hot)^(1/0.9)，其中 N_hot 是热门对象阈值。若 N_hot=100，h_min ≈ 500 * (1000)^(1.11) ≈ 500 * 12,000 ≈ 6,000,000 req/day，用于验证长尾部分的贡献是否可忽略。

## Corrected Claim

热度分布的截断修正：由于 N 有限，Pareto 分布需在 h_min 处截断。h_min = h_max * (N / N_hot)^(1/0.9)，其中 N_hot 是热门对象阈值。若 N_hot=100，N=1000，h_max=500，则 h_min ≈ 500 * (1000)^(1.11) ≈ 500 * 10.46 ≈ 5230 req/day。

## Evidence

父节点级核验通过：正交+完备+无冗余（子节点1聚焦于数值计算的纠错（从错误值6M修正为正确值1.07M），子节点2聚焦于该修正值对后续理论推导（LRU命中率下界/热度集中度）的具体影响。两者在逻辑上是‘纠错’与‘应用’的关系，内容不重叠且互补，共同完整覆盖了父节点中关于‘截断修正’及其‘验证长尾贡献’的核心意图。没有发现冗余的参数化问题。）
