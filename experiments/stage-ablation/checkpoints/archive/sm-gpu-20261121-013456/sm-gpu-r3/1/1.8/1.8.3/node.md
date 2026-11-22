# N73: FP8 精度下总显存需求下限计算：27 GB (权重) + 4.3 GB (KV Cache, GQA, 假设KV也FP8) + 3 GB (激活/缓冲) = 

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N14

## Claim

FP8 精度下总显存需求下限计算：27 GB (权重) + 4.3 GB (KV Cache, GQA, 假设KV也FP8) + 3 GB (激活/缓冲) = 34.3 GB，需 48GB 显存卡 (如 2x4090 或 1xW7900) 方可支持

## Corrected Claim

FP8 精度下总显存需求下限计算：27 GB (权重) + 4.3 GB (KV Cache, GQA, 假设KV也FP8) + 3 GB (激活/缓冲) = 34.3 GB，需 48GB 显存卡 (如 2x4090 或 1xW7900) 方可支持

## Evidence

父节点级核验通过：正交+完备+无冗余（子节点分别对应权重、KV Cache和激活/缓冲三个显存组成部分，彼此独立且无重叠；三者之和（27+4.29+3.0≈34.3 GB）精确匹配父节点中的总显存下限计算，覆盖了所有关键方面，且各部分计算逻辑清晰、参数明确，无冗余。）
