# N38: 修正后的单卡可用于KV Cache的有效显存上限为：16GB (总) - 3.375GB (权重) - 1.5GB (激活) ≈ 11.125 GB/卡。

- **status**: pending
- **level**: L3
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N7

## Claim

修正后的单卡可用于KV Cache的有效显存上限为：16GB (总) - 3.375GB (权重) - 1.5GB (激活) ≈ 11.125 GB/卡。

## Corrected Claim

修正后的单卡可用于KV Cache的有效显存上限为：16GB (总) - 3.375GB (权重) - 1.5GB (激活) ≈ 11.125 GB/卡。

## Evidence

父节点级核验未通过：不完备, 有冗余（子节点本质上是同一公式在不同量化参数下的计算实例，属于参数变体而非独立概念，存在结构性冗余；且父节点明确给出了11.125GB的结论，子节点未包含该基准值的直接陈述，导致逻辑闭环不完整。）
