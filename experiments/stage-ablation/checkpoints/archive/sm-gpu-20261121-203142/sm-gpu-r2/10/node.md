# N33: 性价比指标定义：在无硬性延迟约束下，性价比核心指标定义为 'Cost per 1000 Generated Tokens' 或 'Cost per 1000 I

- **status**: verified
- **level**: L2
- **source**: search
- **edge_type**: quotient
- **rework_count**: 1
- **parent_ids**: (root)

## Claim

性价比指标定义：在无硬性延迟约束下，性价比核心指标定义为 'Cost per 1000 Generated Tokens' 或 'Cost per 1000 Input Tokens (Prefill)'。由于延迟非约束，应优先优化吞吐量(TPS)而非首Token延迟(TTFT)，因此显存带宽(Memory Bandwidth)比计算算力(FLOPS)对生成阶段性价比影响更大。

## Corrected Claim

在无硬性延迟约束下，性价比核心指标定义为 'Cost per 1000 Generated Tokens'。由于延迟非约束，应优先优化吞吐量(TPS)，此时显存带宽(Memory Bandwidth)是决定生成阶段成本的关键瓶颈，比计算算力(FLOPS)影响更大。

## Evidence

父节点级核验通过：正交+完备+无冗余（子节点分别从物理性能极限（带宽/计算）、总拥有成本（TCO）、特定场景瓶颈（Prefill）以及核心指标计算公式四个维度展开，彼此独立且互补，无逻辑重叠或矛盾。）

## Retrieval Sources

- {'url': 'https://zhuanlan.zhihu.com/p/1993849381653337929&rut=9820a984863f1c85e1f11a1dfc68b19c7819b0b2235d85074ba64f86e9258248', 'type': 'ddg', 'title': '问号屋：如何构建企业价格效率变量？ - 知乎'}
