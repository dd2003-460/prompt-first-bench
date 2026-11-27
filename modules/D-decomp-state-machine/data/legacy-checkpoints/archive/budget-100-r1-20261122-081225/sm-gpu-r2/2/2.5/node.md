# N20: Qwen3-27B 模型在 W4A16 (4-bit weights, 16-bit activations) 精度下的权重文件大小约为 13.5 GB (27

- **status**: verified
- **level**: L2
- **source**: given
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N2

## Claim

Qwen3-27B 模型在 W4A16 (4-bit weights, 16-bit activations) 精度下的权重文件大小约为 13.5 GB (27B * 0.5 bytes)。

## Corrected Claim

Qwen3-27B 模型在 W4A16 (4-bit weights, 16-bit activations) 精度下的权重文件大小约为 13.5 GB (27B * 0.5 bytes)。

## Evidence

父节点级核验通过：正交+完备+无冗余（只有一个子节点，不存在子节点间的正交性或冗余问题。该子节点不仅复述了父节点的核心计算逻辑（27B * 0.5 bytes），还补充了实际文件大小略大于理论值的工程细节（量化缩放因子），覆盖了父节点陈述中的隐含前提和实际偏差，信息完备且无冗余。）
