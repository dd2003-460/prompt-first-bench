# N6: 缓存容量占比 (Cache-to-Data Ratio) C/D = 128GB / (100,000 × E[Size])，其中 E[Size] = (α-1

- **status**: verified
- **level**: L2
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 1
- **parent_ids**: N1, N2, N3

## Claim

缓存容量占比 (Cache-to-Data Ratio) C/D = 128GB / (100,000 × E[Size])，其中 E[Size] = (α-1)/(α-1.1) × S_min，取 S_min=1KB 计算得 C/D ≈ 0.0094 (0.94%)，[待核验] S_min 实际值。

## Corrected Claim

缓存容量占比 C/D 的计算依赖于 E[Size] 的准确估计。若采用标准 Zipf 分布模型，E[Size] 应基于分布参数和截断范围重新推导，而非使用给定的简化公式。建议核实 S_min 的实际值及 E[Size] 的计算方法。

## Evidence

父节点级核验通过：正交+完备+无冗余（子节点逻辑链条清晰且互不重叠：节点1计算基础参数（均值），节点2推导总量，节点3得出修正后的核心指标（C/D），节点4解释原错误根源。四者分别对应‘输入计算’、‘中间量推导’、‘结果修正’和‘错误归因’，无逻辑矛盾或重复。）

## Search Query

Pareto distribution mean size calculation edge CDN object storage
