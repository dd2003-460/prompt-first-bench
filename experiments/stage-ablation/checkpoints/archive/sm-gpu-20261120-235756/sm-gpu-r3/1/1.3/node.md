# N9: BF16精度下Qwen3-27B权重存储需求为54.36GB（27.18B × 2 bytes），作为高精度基线用于对比量化损失。

- **status**: pending
- **level**: L2
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N1

## Claim

BF16精度下Qwen3-27B权重存储需求为54.36GB（27.18B × 2 bytes），作为高精度基线用于对比量化损失。

## Corrected Claim

BF16精度下Qwen3-27B权重存储需求为54.36GB（27.18B × 2 bytes），作为高精度基线用于对比量化损失。

## Evidence

父节点级核验未通过：不完备（子节点之间存在主题偏差和范围溢出。父节点仅关注BF16基线的存储需求及其作为对比基准的角色，但子节点1引入了MoE架构对计算参数量的影响（偏离了纯存储基线的定义），子节点2引入了FP8量化对比及具体显卡型号（24GB/32GB）的适用性分析，这超出了父节点‘BF16权重存储需求’的范围，属于扩展性信息而非对父节点本身的分解。）
