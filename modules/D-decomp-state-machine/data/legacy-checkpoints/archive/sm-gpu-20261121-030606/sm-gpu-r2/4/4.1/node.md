# N19: Qwen3-27B模型在BF16精度下的权重存储容量需求为54GB，在FP8精度下为27GB，在INT8精度下为27GB，在NVFP4精度下为13.5GB，在W

- **status**: pending
- **level**: L2
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N4, N5, N6

## Claim

Qwen3-27B模型在BF16精度下的权重存储容量需求为54GB，在FP8精度下为27GB，在INT8精度下为27GB，在NVFP4精度下为13.5GB，在W4A16精度下为13.5GB

## Corrected Claim

Qwen3-27B模型在BF16精度下的权重存储容量需求为54GB，在FP8精度下为27GB，在INT8精度下为27GB，在NVFP4精度下为13.5GB，在W4A16精度下为13.5GB

## Evidence

父节点级核验未通过：非正交, 不完备, 有冗余（1. 正交性失败：子节点2和子节点3逻辑结构高度重复，均为‘修正特定精度下的显存计算矛盾’，且都引用了相同的错误值（13.5GB）和相同的归因逻辑（混淆4-bit数据），应合并。2. 完备性失败：父节点包含5种精度（BF16, FP8, INT8, NVFP4, W4A16）的显存需求，但子节点仅解释了FP8和INT8的修正，完全缺失了BF16、NVFP4和W4A16的计算依据或来源说明，导致父节点中的其他数据点缺乏支撑。3. 冗余严重：子节点2和3本质上是同一类错误（将8-bit误算为4-bit）的重复实例，且子节点1仅提供了参数量这一单一变量，未形成完整的计算逻辑链。）
