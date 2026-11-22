# N150: A100 80GB PCIe 在 BF16 精度、32K 上下文（KV Cache 32.77 GB）下的理论 Decode 吞吐量为 2039 / (32.7

- **status**: pending
- **level**: L4
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N45

## Claim

A100 80GB PCIe 在 BF16 精度、32K 上下文（KV Cache 32.77 GB）下的理论 Decode 吞吐量为 2039 / (32.77 + 54) ≈ 23.5 tokens/s，该计算未包含 PCIe 互联开销（单卡无此开销），但需乘以 0.7 的效率系数得到约 16.5 tokens/s 的保守估计。

## Corrected Claim

A100 80GB PCIe 在 BF16 精度、32K 上下文（KV Cache 32.77 GB）下的理论 Decode 吞吐量为 2039 / (32.77 + 54) ≈ 23.5 tokens/s，该计算未包含 PCIe 互联开销（单卡无此开销），但需乘以 0.7 的效率系数得到约 16.5 tokens/s 的保守估计。

## Evidence

父节点级核验未通过：非正交（子节点之间存在逻辑矛盾：子节点2修正了KV Cache大小并计算了新的理论吞吐量（32.9 tokens/s），而父节点仍基于错误的32.77 GB计算（23.5 tokens/s）。子节点1、2、3构成了一个连贯的修正链，但父节点与子节点2在核心数据（KV Cache大小和理论吞吐量）上不一致，导致子节点2与父节点隐含的前提冲突。此外，子节点3依赖于子节点2的结果，而非父节点的结果，这进一步表明父节点本身是错误的，而子节点集合实际上是在纠正父节点，而非分解父节点。）
