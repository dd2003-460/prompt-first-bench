# N140: 覆盖效率 $\eta_{coverage}$ 的 Zipf 分布解析近似：$\eta_{coverage} \approx \sum_{i=1}^{N_{pop

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N38

## Claim

覆盖效率 $\eta_{coverage}$ 的 Zipf 分布解析近似：$\eta_{coverage} \approx \sum_{i=1}^{N_{pop}} P_{pop_i}$，其中 $P_{pop_i}$ 为第 $i$ 个 POP 覆盖区域的流量占比；基于 N34 的 Top 5 省份占比 65%-70% 及 10 个 POP 的 K-Median 选址，$\eta_{coverage}$ 的理论下限为 Top 5 省份占比（65%），上限受限于剩余省份的地理分散度（预估 80%-85%）。

## Corrected Claim

覆盖效率 $\eta_{coverage}$ 的 Zipf 分布解析近似：$\eta_{coverage} \approx \sum_{i=1}^{N_{pop}} P_{pop_i}$，其中 $P_{pop_i}$ 为第 $i$ 个 POP 覆盖区域的流量占比；基于 N34 的 Top 5 省份占比 65%-70% 及 10 个 POP 的 K-Median 选址，$\eta_{coverage}$ 的理论下限为 Top 5 省份占比（65%），上限受限于剩余省份的地理分散度（预估 80%-85%）。

## Evidence

先验知识/题面给定，逻辑校验通过：覆盖效率定义为各POP覆盖区域流量占比之和，基于Zipf分布特性，Top 5省份占比构成理论下限，剩余省份分散度决定上限，数值量级（65%-85%）符合地理与流量分布常识。
