# N164: 双RTX 4090 (INT8)在32K上下文、batch_size=1下的理论推理吞吐量(tokens/s) = (2×1008 GB/s × 0.65效率系

- **status**: pending
- **level**: L3
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 1
- **parent_ids**: N79

## Claim

双RTX 4090 (INT8)在32K上下文、batch_size=1下的理论推理吞吐量(tokens/s) = (2×1008 GB/s × 0.65效率系数) / (13.5GB权重 + 5.2GB KV Cache + 2.5GB激活) ≈ 51.4 tokens/s，考虑PCIe互联65%效率折损

## Corrected Claim

双RTX 4090 (INT8)在32K上下文、batch_size=1下的理论推理吞吐量受内存带宽限制，估算值约为51.4 tokens/s，但实际吞吐量可能因计算瓶颈和通信开销而低于此值。

## Evidence

父节点级核验未通过：非正交, 不完备, 有冗余（子节点2直接依赖子节点1的修正值进行计算，两者存在强依赖关系而非正交；且父节点中的'PCIe互联效率'在子节点中未被独立分析或修正，导致覆盖不全。子节点1和2本质上是同一修正链条中的中间步骤和最终结果，存在冗余。）
