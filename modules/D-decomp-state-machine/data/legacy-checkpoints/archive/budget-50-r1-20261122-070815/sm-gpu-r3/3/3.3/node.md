# N20: PCIe 互联带宽（单卡 vs 多卡）影响多卡方案的通信开销，需评估 2x 消费卡 vs 1x 数据卡在 PCIe 4.0/5.0 下的吞吐损失

- **status**: verified
- **level**: L2
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N3

## Claim

PCIe 互联带宽（单卡 vs 多卡）影响多卡方案的通信开销，需评估 2x 消费卡 vs 1x 数据卡在 PCIe 4.0/5.0 下的吞吐损失

## Corrected Claim

PCIe 互联带宽（单卡 vs 多卡）影响多卡方案的通信开销，需评估 2x 消费卡 vs 1x 数据卡在 PCIe 4.0/5.0 下的吞吐损失

## Evidence

父节点级核验通过：正交+完备+无冗余（子节点分别覆盖了基础理论带宽参数、2x消费卡方案的具体瓶颈分析、以及1x数据卡方案的优势与对比结论，三者逻辑层层递进且互不重叠，完整覆盖了父节点关于'单卡vs多卡'及'PCIe 4.0/5.0'的核心评估需求。）
