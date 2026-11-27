# N72: BF16 精度下总显存需求下限计算：54 GB (权重) + 4.3 GB (KV Cache, GQA) + 3 GB (激活/缓冲) = 61.3 GB，因

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N14

## Claim

BF16 精度下总显存需求下限计算：54 GB (权重) + 4.3 GB (KV Cache, GQA) + 3 GB (激活/缓冲) = 61.3 GB，因此单卡 24GB 或 48GB 无法运行 BF16 全精度 32K 上下文

## Corrected Claim

BF16 精度下总显存需求下限计算：54 GB (权重) + 4.3 GB (KV Cache, GQA) + 3 GB (激活/缓冲) = 61.3 GB，因此单卡 24GB 或 48GB 无法运行 BF16 全精度 32K 上下文

## Evidence

父节点级核验通过：正交+完备+无冗余（子节点基于量化策略（权重/KV精度）和注意力机制进行了清晰的正交划分，分别代表了性能/成本的不同权衡工作点，无逻辑矛盾或重复。父节点仅陈述了BF16全精度（即子节点C）的显存下限结论，子节点A和B补充了通过量化降低显存需求的可行替代方案，共同构成了完整的显存需求与硬件可行性分析，覆盖了父节点隐含的‘如何优化’及‘硬件匹配’方面。）
