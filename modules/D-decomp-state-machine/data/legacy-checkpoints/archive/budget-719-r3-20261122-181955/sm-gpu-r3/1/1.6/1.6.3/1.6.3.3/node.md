# N217: CPU 推理方案中，FP16/BF16 矩阵乘法无法利用 AMX/AVX-512 VNNI 的整数加速路径，必须使用 FMA (Fused Multiply-A

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N67

## Claim

CPU 推理方案中，FP16/BF16 矩阵乘法无法利用 AMX/AVX-512 VNNI 的整数加速路径，必须使用 FMA (Fused Multiply-Add) 指令，其吞吐量仅为 INT8 路径的 1/2 至 1/4，因此 CPU 方案必须采用 INT4/INT8 量化才能发挥硬件优势 [待核验]

## Corrected Claim

CPU 推理方案中，FP16/BF16 矩阵乘法无法利用 AMX/AVX-512 VNNI 的整数加速路径，必须使用 FMA (Fused Multiply-Add) 指令，其吞吐量仅为 INT8 路径的 1/2 至 1/4，因此 CPU 方案必须采用 INT4/INT8 量化才能发挥硬件优势 [待核验]

## Evidence

先验知识/题面给定，逻辑校验通过：AMX/AVX-512 VNNI 专为整数（INT8/INT4）设计，FP16/BF16 需走 FMA 路径，吞吐量确实显著低于整数路径（通常约为 1/2 至 1/4），符合硬件架构事实。
