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

父节点级核验未通过：有冗余（子节点在逻辑上正交且覆盖了所有精度场景，但存在明显的结构性冗余。子节点2、3、4遵循完全相同的计算模式（权重+KV+开销=总显存），仅数值不同。这种‘列表式’分解未能抽象出通用的计算逻辑，导致信息密度低且难以维护。）
