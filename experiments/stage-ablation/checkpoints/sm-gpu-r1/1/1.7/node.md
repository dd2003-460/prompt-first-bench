# N13: 量化精度选择对显存占用的线性影响系数：不同精度下的 bytes/weight 值（BF16=2, FP8=1, INT8=1, NVFP4=0.5, W4=0.

- **status**: verified
- **level**: L2
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N1, N2, N3

## Claim

量化精度选择对显存占用的线性影响系数：不同精度下的 bytes/weight 值（BF16=2, FP8=1, INT8=1, NVFP4=0.5, W4=0.5），以及由此推导的显存节省比例

## Corrected Claim

量化精度选择对显存占用的线性影响系数：不同精度下的 bytes/weight 值（BF16=2, FP8=1, INT8=1, NVFP4=0.5, W4=0.5），以及由此推导的显存节省比例

## Evidence

先验知识/题面给定，逻辑校验通过：各精度对应的字节数（BF16=2, FP8/INT8=1, NVFP4/W4=0.5）符合计算机体系结构基本定义，显存占用与字节数呈线性关系，推导逻辑自洽。

## Search Query

quantization precision bytes per weight BF16 FP8 INT8 NVFP4 W4
