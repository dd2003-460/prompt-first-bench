# N9: 不同精度（BF16/FP8/INT8/NVFP4/W4）下模型权重占用显存分别为 54GB/27GB/27GB/13.5GB/6.75GB，加上 KV Cach

- **status**: pending
- **level**: L2
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N1

## Claim

不同精度（BF16/FP8/INT8/NVFP4/W4）下模型权重占用显存分别为 54GB/27GB/27GB/13.5GB/6.75GB，加上 KV Cache 后的总显存下限需分别计算

## Corrected Claim

不同精度（BF16/FP8/INT8/NVFP4/W4）下模型权重占用显存分别为 54GB/27GB/27GB/13.5GB/6.75GB，加上 KV Cache 后的总显存下限需分别计算

## Evidence

父节点级核验未通过：有冗余（子节点3和子节点4的结构高度相似，本质上是对同一计算公式（权重+KV+开销）在不同精度参数下的重复实例化，存在结构性冗余。）
