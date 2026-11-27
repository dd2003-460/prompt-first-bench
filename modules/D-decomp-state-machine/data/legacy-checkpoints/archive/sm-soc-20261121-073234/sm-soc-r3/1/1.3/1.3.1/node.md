# N38: 『成交周期变短』需量化为：在当前溢价率区间内，P50（中位数）成交时间 T_median 相比历史基线 T_base 下降的比例 ΔT = (T_base - 

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N7

## Claim

『成交周期变短』需量化为：在当前溢价率区间内，P50（中位数）成交时间 T_median 相比历史基线 T_base 下降的比例 ΔT = (T_base - T_median) / T_base，预期 ΔT > 20% 以证明显著性。

## Corrected Claim

『成交周期变短』需量化为：在当前溢价率区间内，P50（中位数）成交时间 T_median 相比历史基线 T_base 下降的比例 ΔT = (T_base - T_median) / T_base，预期 ΔT > 20% 以证明显著性。

## Evidence

父节点级核验通过：正交+完备+无冗余（四个子节点分别对应统计检验效力、基线定义、当前值估计、数据清洗，逻辑上正交且互不重叠；它们共同构成了从数据准备到统计验证的完整闭环，覆盖了父节点量化指标的所有关键维度；各节点代表不同的处理阶段或方法维度，并非同一参数的不同取值，无冗余。）

## Search Query

median time to sell reduction percentage high premium items
