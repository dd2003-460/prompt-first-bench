# N41: 不同精度下模型权重显存占用的精确计算：BF16=54GB, FP8=27GB, INT8=27GB, NVFP4=13.5GB, W4=6.75GB。注：NVF

- **status**: pending
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N9

## Claim

不同精度下模型权重显存占用的精确计算：BF16=54GB, FP8=27GB, INT8=27GB, NVFP4=13.5GB, W4=6.75GB。注：NVFP4 为 4-bit 浮点，W4 为 4-bit 整型，两者显存占用理论值相同，但 NVFP4 可能因存储 scale 因子而略有增加（约 5-10%）。

## Corrected Claim

不同精度下模型权重显存占用的精确计算：BF16=54GB, FP8=27GB, INT8=27GB, NVFP4=13.5GB, W4=6.75GB。注：NVFP4 为 4-bit 浮点，W4 为 4-bit 整型，两者显存占用理论值相同，但 NVFP4 可能因存储 scale 因子而略有增加（约 5-10%）。

## Evidence

父节点级核验未通过：有冗余（子节点在数值上正交且覆盖了父节点所有精度维度，但存在结构性冗余。子节点1（BF16）与子节点2（FP8/INT8）的计算逻辑高度同构（均为 P × bytes/param），且子节点2将FP8和INT8合并处理，忽略了父节点中两者虽数值相同但可能存在的量化策略差异（如Embedding层是否统一保留BF16）。更重要的是，子节点1和2可以抽象为同一个参数化公式的不同实例，导致知识碎片化。）
