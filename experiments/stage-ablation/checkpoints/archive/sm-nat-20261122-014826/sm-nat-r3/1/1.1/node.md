# N6: 缓存容量占比 (Cache-to-Data Ratio) C/D = 128GB / (100,000 × E[Size])，其中 E[Size] = (α-1

- **status**: pending
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

父节点级核验未通过：非正交, 有冗余（子节点存在严重的逻辑依赖和计算冗余。节点2（总数据量）和节点3（修正后占比）本质上是节点1（均值计算）的直接算术推论，属于同一推导链条的不同步骤，而非独立正交的概念。此外，节点4（错误根源）与节点1（正确计算）在逻辑上是对立验证关系，但节点3已经隐含了节点1的结果，导致节点1、2、3高度耦合，未形成正交的知识块。）

## Search Query

Pareto distribution mean size calculation edge CDN object storage
