# N18: 用户地理分布熵 H_geo = -Σ p_i log2(p_i)，其中 p_i 为第 i 个省份/区域的流量占比；该指标决定自建 POP 点的最优覆盖半径与回源

- **status**: pending
- **level**: L2
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N4

## Claim

用户地理分布熵 H_geo = -Σ p_i log2(p_i)，其中 p_i 为第 i 个省份/区域的流量占比；该指标决定自建 POP 点的最优覆盖半径与回源距离

## Corrected Claim

用户地理分布熵 H_geo = -Σ p_i log2(p_i)，其中 p_i 为第 i 个省份/区域的流量占比；该指标决定自建 POP 点的最优覆盖半径与回源距离

## Evidence

父节点级核验未通过：不完备（子节点分别描述了覆盖半径和回源距离两个不同维度的物理量，彼此正且不重复。但父节点明确定义 H_geo 为流量占比的熵，子节点完全遗漏了 H_geo 的计算基础（即流量分布 p_i 的获取与统计），导致分解在‘输入数据’层面不完备，仅覆盖了‘输出推导’层面。）
