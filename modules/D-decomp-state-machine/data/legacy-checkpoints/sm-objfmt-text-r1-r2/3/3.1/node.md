# N16: 消费级 GPU 当前值得考虑的完整候选集：RTX 4090 (24GB), RTX 4080 Super (16GB), RTX 3090 (24GB), RT

- **status**: pending
- **level**: L2
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N3

## Claim

消费级 GPU 当前值得考虑的完整候选集：RTX 4090 (24GB), RTX 4080 Super (16GB), RTX 3090 (24GB), RTX 3060 12GB (排除，容量不足)，需验证 24GB 是否为 27B BF16 最低门槛

## Corrected Claim

消费级 GPU 当前值得考虑的完整候选集：RTX 4090 (24GB), RTX 4080 Super (16GB), RTX 3090 (24GB), RTX 3060 12GB (排除，容量不足)，需验证 24GB 是否为 27B BF16 最低门槛

## Evidence

父节点级核验未通过：非正交, 有冗余（子节点存在逻辑重叠和冗余：节点1和节点3都详细描述了24GB显存下的低精度推理限制，内容高度相似；节点4独立分析了24GB显存的通用约束，这与节点1、3中的具体分析重复。此外，节点1和节点3本质上是同一类硬件（24GB VRAM）的不同实例，应合并或作为参数处理，而非正交节点。）
