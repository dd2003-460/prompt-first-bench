# N140: FP8 权重在 H100/MI300 硬件上的对齐 (Alignment) 开销：NVIDIA Tensor Core 要求 FP8 张量维度对齐到 16 字节

- **status**: pending
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N40

## Claim

FP8 权重在 H100/MI300 硬件上的对齐 (Alignment) 开销：NVIDIA Tensor Core 要求 FP8 张量维度对齐到 16 字节或 32 字节边界，对于 27B 参数模型，Padding 开销约为 0.1-0.2GB（约 0.4-0.7%），具体取决于层权重矩阵形状（如 4096x4096 矩阵对齐后无额外 padding，但非对齐维度需填充）。

## Corrected Claim

FP8 权重在 H100/MI300 硬件上的对齐 (Alignment) 开销：NVIDIA Tensor Core 要求 FP8 张量维度对齐到 16 字节或 32 字节边界，对于 27B 参数模型，Padding 开销约为 0.1-0.2GB（约 0.4-0.7%），具体取决于层权重矩阵形状（如 4096x4096 矩阵对齐后无额外 padding，但非对齐维度需填充）。

## Evidence

父节点级核验未通过：非正交, 不完备, 有冗余（1. 正交性差：子节点4和子节点5高度重叠，均在讨论FP8对齐开销为0的问题，且逻辑重复；子节点3引入了INT4/其他开销，与父节点FP8主题偏离。2. 完备性不足：父节点核心是FP8对齐开销，但子节点1、2、3讨论的是INT4量化、CUDA Workspace和KV Cache，完全偏离了'FP8权重对齐'这一特定主题。3. 冗余严重：子节点4和5可以合并；子节点6和7讨论的Scale/Metadata开销虽然相关，但属于量化参数存储而非'对齐Padding'，且计算细节过于琐碎，可简化。）

## Search Query

NVIDIA Tensor Core FP8 alignment padding overhead bytes
