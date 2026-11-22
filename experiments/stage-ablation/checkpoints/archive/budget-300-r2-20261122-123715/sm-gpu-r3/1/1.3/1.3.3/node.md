# N44: Mac Studio M2 Ultra 192GB 的统一内存架构允许模型权重、KV Cache 和激活值共享同一内存池，避免了多卡互联带宽瓶颈，但内存带宽 8

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N7

## Claim

Mac Studio M2 Ultra 192GB 的统一内存架构允许模型权重、KV Cache 和激活值共享同一内存池，避免了多卡互联带宽瓶颈，但内存带宽 800GB/s 低于 HBM 的 2039GB/s（A100）或 GDDR6X 的 1008GB/s（RTX 4090），吞吐量受限

## Corrected Claim

Mac Studio M2 Ultra 192GB 的统一内存架构允许模型权重、KV Cache 和激活值共享同一内存池，避免了多卡互联带宽瓶颈，但内存带宽 800GB/s 低于 HBM 的 2039GB/s（A100）或 GDDR6X 的 1008GB/s（RTX 4090），吞吐量受限

## Evidence

父节点级核验通过：正交+完备+无冗余（三个子节点分别聚焦于容量可行性（无Offload风险）、性能瓶颈（带宽对比与吞吐估算）以及能效/TCO（功耗与成本），维度清晰且互不重叠。父节点提到的'统一内存架构'、'避免多卡瓶颈'（隐含在单卡大容量中）、'带宽限制'及'具体硬件参数'均被覆盖。虽然能效比不是父节点直接强调的核心痛点，但作为统一内存架构相对于独立显卡的潜在优势/劣势分析，属于合理的补充维度，不构成冗余。）
