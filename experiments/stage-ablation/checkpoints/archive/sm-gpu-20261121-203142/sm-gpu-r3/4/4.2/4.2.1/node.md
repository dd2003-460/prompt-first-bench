# N79: 单卡方案的5年总电力成本计算公式：Cost_electricity_single = TDP_gpu * 1.1 (PSU效率损耗) * 24h * 365d 

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N22

## Claim

单卡方案的5年总电力成本计算公式：Cost_electricity_single = TDP_gpu * 1.1 (PSU效率损耗) * 24h * 365d * 5y * 0.10 (USD/kWh)；以RTX 4090 (450W)为例，计算结果约为 $1,001.25。

## Corrected Claim

单卡方案的5年总电力成本计算公式：Cost_electricity_single = TDP_gpu * 1.1 (PSU效率损耗) * 24h * 365d * 5y * 0.10 (USD/kWh)；以RTX 4090 (450W)为例，计算结果约为 $1,001.25。

## Evidence

父节点级核验通过：正交+完备+无冗余（子节点分别针对功耗模型（负载加权）、电源效率参数（PSU系数）和电价参数（地域差异）进行独立修正，三者分别对应公式中的不同变量，逻辑上互不重叠且无矛盾。它们共同覆盖了父节点公式中所有可修正的关键假设，且每个子节点代表不同的物理或经济维度，不构成冗余。）
