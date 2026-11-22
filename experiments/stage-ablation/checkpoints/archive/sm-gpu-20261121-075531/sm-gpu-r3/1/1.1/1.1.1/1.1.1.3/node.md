# N133: 基于精确参数量 27.1B，各精度下的纯权重字节数 Bytes_Weight 计算为：BF16 = 27.1 * 2 = 54.2GB，FP8/INT8 = 2

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N35

## Claim

基于精确参数量 27.1B，各精度下的纯权重字节数 Bytes_Weight 计算为：BF16 = 27.1 * 2 = 54.2GB，FP8/INT8 = 27.1 * 1 = 27.1GB，W4 = 27.1 * 0.5 = 13.55GB。

## Corrected Claim

基于精确参数量 27.1B，各精度下的纯权重字节数 Bytes_Weight 计算为：BF16 = 27.1 * 2 = 54.2GB，FP8/INT8 = 27.1 * 1 = 27.1GB，W4 = 27.1 * 0.5 = 13.55GB。

## Evidence

先验知识/题面给定，逻辑校验通过：参数量27.1B乘以各精度字节数（BF16=2, FP8/INT8=1, W4=0.5）计算结果准确，量纲与数值均合理。
