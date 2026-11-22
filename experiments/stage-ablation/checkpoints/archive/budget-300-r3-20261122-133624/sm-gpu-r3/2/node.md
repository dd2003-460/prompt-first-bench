# N2: 性能-成本效率度量：覆盖不同精度下的推理吞吐量（tokens/s）、硬件购置与运行TCO结构、以及单位token生成成本，作为排序键（Ranking Key）比

- **status**: pending
- **level**: L1
- **source**: given
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: (root)

## Claim

性能-成本效率度量：覆盖不同精度下的推理吞吐量（tokens/s）、硬件购置与运行TCO结构、以及单位token生成成本，作为排序键（Ranking Key）比较可行方案的性价比。

## Evidence

父节点级核验未通过：不完备, 有冗余（子节点3和4在逻辑上是同构的（都是'单位成本=TCO/吞吐量'），仅参数不同，存在结构冗余；且父节点明确提到'覆盖不同精度'，但子节点仅列出了BF16和INT8两种特定硬件组合，缺乏对'其他精度/硬件组合'的通用覆盖或说明，完备性不足。）
