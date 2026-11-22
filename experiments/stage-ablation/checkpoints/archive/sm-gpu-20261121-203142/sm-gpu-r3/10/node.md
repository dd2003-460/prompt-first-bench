# N33: 性价比指标定义：在无硬性延迟约束下，性价比核心指标定义为 'Cost per 1000 Generated Tokens' 或 'Cost per 1000 I

- **status**: pending
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

父节点级核验未通过：不完备（子节点在内容上正交，分别覆盖了生成速度物理极限（带宽瓶颈）、总拥有成本（TCO）、Prefill性能（计算瓶颈）以及成本计算公式。但存在两个主要问题：1. 完备性不足：父节点强调'性价比'指标，但子节点3（Prefill）和子节点4（公式）仅提供了局部数据或通用公式，未将M2 Ultra的具体性能数据代入公式计算出最终的'Cost per 1000 Tokens'数值，导致无法直接验证'性价比'结论；2. 逻辑一致性：子节点1声称实测15-25 tokens/s中15-18符合物理极限，而子节点3暗示M2 Ultra在生成阶段因带宽优势'可接受'，但未明确该'可接受'是基于哪个具体TPS值，且子节点4指出CapEx是主要成本驱动，子节点2中M2 Ultra CapEx高于4090方案，这直接影响了最终性价比结论，但子节点间缺乏对最终性价比排名的综合推导。）

## Retrieval Sources

- {'url': 'https://zhuanlan.zhihu.com/p/1993849381653337929&rut=9820a984863f1c85e1f11a1dfc68b19c7819b0b2235d85074ba64f86e9258248', 'type': 'ddg', 'title': '问号屋：如何构建企业价格效率变量？ - 知乎'}
