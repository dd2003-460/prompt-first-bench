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

父节点级核验未通过：不完备, 有冗余（1. 完备性不足：父节点明确列出了5种精度（BF16, FP8, INT8, NVFP4, W4A16）的存储需求，但子节点仅覆盖了基础参数量、FP8和INT8的修正，完全缺失了BF16、NVFP4和W4A16的验证或说明，导致分解未覆盖父节点所有关键方面。2. 冗余/结构问题：子节点2和子节点3逻辑高度重复，均为“指出某节点错误 -> 计算正确值(27GB) -> 判定原节点混淆了4-bit数据”。这两个子节点本质上是在修正同一类错误（混淆8-bit与4-bit量化），可以合并为一个关于“8-bit精度（FP8/INT8）权重计算修正”的节点，或者将具体的数值计算下沉，保持子节点间的独立语义。）
