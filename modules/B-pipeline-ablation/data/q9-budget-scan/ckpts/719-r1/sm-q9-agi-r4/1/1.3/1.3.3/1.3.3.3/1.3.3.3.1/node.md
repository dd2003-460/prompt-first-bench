# N414: FP4->FP16 反量化 kernel 的算术强度 (Arithmetic Intensity) 计算：AI = FLOPs / Bytes_Moved。对于

- **status**: verified
- **level**: L5
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N140

## Claim

FP4->FP16 反量化 kernel 的算术强度 (Arithmetic Intensity) 计算：AI = FLOPs / Bytes_Moved。对于 27B 模型，每 token 前向 FLOPs ≈ 2 * 27e9 = 54 GFLOPs；FP4 权重读取量 ≈ 27e9 * 0.5 bytes = 13.5 GB。理想 AI = 54e9 / 13.5e9 = 4 FLOPs/Byte。

## Corrected Claim

FP4->FP16 反量化 kernel 的算术强度 (Arithmetic Intensity) 计算：AI = FLOPs / Bytes_Moved。对于 27B 模型，每 token 前向 FLOPs ≈ 2 * 27e9 = 54 GFLOPs；FP4 权重读取量 ≈ 27e9 * 0.5 bytes = 13.5 GB。理想 AI = 54e9 / 13.5e9 = 4 FLOPs/Byte。

## Evidence

先验知识/题面给定，逻辑校验通过：27B模型每token前向FLOPs约为2*参数量=54G，FP4权重读取量为参数量*0.5字节=13.5GB，算术强度AI=54G/13.5G=4 FLOPs/Byte，计算过程符合定义且量级合理。
