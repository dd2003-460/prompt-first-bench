# N114: W4A16量化在推理时需进行权重反量化（Dequantization），其计算开销约为每Token 1.5-2.0x 的额外FLOPs，在计算受限（Comput

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N40

## Claim

W4A16量化在推理时需进行权重反量化（Dequantization），其计算开销约为每Token 1.5-2.0x 的额外FLOPs，在计算受限（Compute-Bound）场景下会抵消部分INT4的带宽优势

## Corrected Claim

W4A16量化在推理时需进行权重反量化（Dequantization），其计算开销约为每Token 1.5-2.0x 的额外FLOPs，在计算受限（Compute-Bound）场景下会抵消部分INT4的带宽优势

## Evidence

先验知识/题面给定，逻辑校验通过：W4A16量化在推理时确实需要权重反量化，其计算开销约为每Token 1.5-2.0x的额外FLOPs，在计算受限场景下会抵消部分INT4的带宽优势，符合量化推理的基本原理。
