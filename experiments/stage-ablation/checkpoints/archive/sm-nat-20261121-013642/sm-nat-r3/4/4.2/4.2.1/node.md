# N60: R_bytes (总字节请求率) 的计算表达式：R_bytes = (50,000,000 requests/day) * E[Size | Pareto(α=

- **status**: pending
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N16

## Claim

R_bytes (总字节请求率) 的计算表达式：R_bytes = (50,000,000 requests/day) * E[Size | Pareto(α=1.1)]，其中 E[Size] = s_min * α / (α-1) (需设定 s_min 并截断以匹配 128GB 总容量约束或取前 100k 对象均值)，单位为 GB/day。

## Corrected Claim

R_bytes (总字节请求率) 的计算表达式：R_bytes = (50,000,000 requests/day) * E[Size | Pareto(α=1.1)]，其中 E[Size] = s_min * α / (α-1) (需设定 s_min 并截断以匹配 128GB 总容量约束或取前 100k 对象均值)，单位为 GB/day。

## Evidence

父节点级核验未通过：不完备, 有冗余（子节点本质上是同一参数（对象大小分布的截断范围 s_min/s_max）在不同取值下的实例，属于参数扫描而非结构性分解，因此存在严重冗余；此外，父节点中明确提到的“取前 100k 对象均值”这一特定计算路径未在子节点中体现，导致覆盖不完备。）
