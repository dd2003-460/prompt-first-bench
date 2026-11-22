# N19: 单卡vs多卡TCO对比框架：TCO = 硬件成本 + 电力成本(5年) + 冷却成本(5年) + 维护成本(5年) + 机会成本(资金占用利息)；对于2×RTX

- **status**: pending
- **level**: L2
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N3

## Claim

单卡vs多卡TCO对比框架：TCO = 硬件成本 + 电力成本(5年) + 冷却成本(5年) + 维护成本(5年) + 机会成本(资金占用利息)；对于2×RTX 4090 vs 1×A100 80GB，需计算5年总拥有成本

## Corrected Claim

单卡vs多卡TCO对比框架：TCO = 硬件成本 + 电力成本(5年) + 冷却成本(5年) + 维护成本(5年) + 机会成本(资金占用利息)；对于2×RTX 4090 vs 1×A100 80GB，需计算5年总拥有成本

## Evidence

父节点级核验未通过：不完备, 有冗余（1. 冗余严重：工作点1、2、3本质上是同一类‘具体硬件配置案例’的不同取值，属于可压缩的参数实例，而非正交的逻辑维度。2. 完备性不足：父节点明确对比对象为 '2×RTX 4090 vs 1×A100 80GB'，但子节点中未包含 A100 80GB 的具体 TCO 计算，反而引入了 L40S 和 H100，导致未覆盖父节点指定的核心对比项。3. 逻辑割裂：子节点4（机会成本）是计算因子，而前三个是计算结果，层级不一致。）

## Search Query

TCO calculation GPU inference 5 year total cost of ownership electricity cooling
