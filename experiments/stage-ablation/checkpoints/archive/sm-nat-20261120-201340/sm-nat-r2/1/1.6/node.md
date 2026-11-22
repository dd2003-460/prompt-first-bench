# N11: 请求热度 Pareto(β=0.9) 的累积分布函数 CDF(r) = (r_min/r)^β，其中 r_min 是最小请求率，前 k 个最热门对象的请求占比 

- **status**: pending
- **level**: L2
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N1, N2, N3

## Claim

请求热度 Pareto(β=0.9) 的累积分布函数 CDF(r) = (r_min/r)^β，其中 r_min 是最小请求率，前 k 个最热门对象的请求占比 = 1 - (k/N)^β（近似，假设对象按热度排序）

## Corrected Claim

请求热度 Pareto(β=0.9) 的累积分布函数 CDF(r) = (r_min/r)^β，其中 r_min 是最小请求率，前 k 个最热门对象的请求占比 = 1 - (k/N)^β（近似，假设对象按热度排序）

## Evidence

父节点级核验未通过：不完备（子节点存在公式错误且未完全覆盖父节点定义的CDF关系。子节点1给出的累积占比公式在β<1时逻辑有误（分母为负，分子项次幂错误，标准Pareto累积质量公式应为 (1 - (k/N)^(1-β)) / (1 - N^(1-β)) 或类似形式，且与父节点给出的简化近似 1-(k/N)^β 不一致，未澄清近似条件）；子节点2计算r_min正确，但两者未涵盖父节点中明确提到的CDF(r) = (r_min/r)^β 这一核心分布函数形式及其推导或验证。）

## Search Query

Pareto distribution CDF request popularity cache
