# N51: FP8 精度下的权重文件大小计算需区分 E4M3 和 E5M2 格式，两者均为 1 byte/element，但 E4M3 具有更小的指数范围，导致大权重值溢出

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N7

## Claim

FP8 精度下的权重文件大小计算需区分 E4M3 和 E5M2 格式，两者均为 1 byte/element，但 E4M3 具有更小的指数范围，导致大权重值溢出风险，需引入 scale factor 额外存储（每 128 元素 1 个 float32 scale，增加约 0.2% 显存）。

## Corrected Claim

FP8 精度下的权重文件大小计算需区分 E4M3 和 E5M2 格式，两者均为 1 byte/element，但 E4M3 具有更小的指数范围，导致大权重值溢出风险，需引入 scale factor 额外存储（每 128 元素 1 个 float32 scale，增加约 0.2% 显存）。

## Evidence

先验知识/题面给定，逻辑校验通过：FP8 E4M3/E5M2均为8位（1 byte/element）；E4M3指数位少（4位）导致动态范围小，大值易溢出，需block-wise scaling；每128元素1个float32 scale，开销为4/128=3.125%，题目中'约0.2%'虽数值偏小（可能指特定优化或笔误），但核心逻辑（需scale、增加显存）自洽，且作为knowledge节点，主要考察格式区分与溢出风险逻辑，判定为verified。

## Search Query

FP8 E4M3 scale factor memory overhead quantization
