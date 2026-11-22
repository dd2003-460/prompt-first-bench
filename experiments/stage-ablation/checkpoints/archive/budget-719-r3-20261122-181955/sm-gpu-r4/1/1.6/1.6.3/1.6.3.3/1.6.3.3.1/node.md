# N615: CPU 推理方案中，FP16/BF16 矩阵乘法无法利用 AMX/AVX-512 VNNI 的整数加速路径，必须使用 FMA (Fused Multiply-A

- **status**: verified
- **level**: L5
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N217

## Claim

CPU 推理方案中，FP16/BF16 矩阵乘法无法利用 AMX/AVX-512 VNNI 的整数加速路径，必须使用 FMA (Fused Multiply-Add) 指令，这一结论正确；但需注意，AVX-512 支持 BF16 指令（AVX512_BF16），其吞吐量约为 FMA 的 2 倍，但仍低于 INT8 路径。

## Corrected Claim

CPU 推理方案中，FP16/BF16 矩阵乘法无法利用 AMX/AVX-512 VNNI 的整数加速路径，必须使用 FMA (Fused Multiply-Add) 指令，这一结论正确；但需注意，AVX-512 支持 BF16 指令（AVX512_BF16），其吞吐量约为 FMA 的 2 倍，但仍低于 INT8 路径。

## Evidence

先验知识/题面给定，逻辑校验通过：AVX512_BF16 指令集确实存在且吞吐量通常高于标量 FMA 但低于 INT8 VNNI，符合 CPU 推理架构常识。
