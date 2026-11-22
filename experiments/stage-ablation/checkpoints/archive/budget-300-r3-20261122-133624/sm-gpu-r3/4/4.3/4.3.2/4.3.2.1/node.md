# N314: RTX 4090 (Ada Lovelace) 的 Tensor Core 仅支持 FP16/BF16/TF32/INT8 硬件矩阵乘法，不支持原生 FP8 (

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N103

## Claim

RTX 4090 (Ada Lovelace) 的 Tensor Core 仅支持 FP16/BF16/TF32/INT8 硬件矩阵乘法，不支持原生 FP8 (E4M3/E5M2) Tensor Core 运算；FP8 推理必须通过软件路径（dequantize 至 FP16/BF16 后计算，或转为 INT8 后计算），因此 FP8 相比 BF16 的吞吐量增益仅来自显存带宽节省（2x），而非计算单元加速。

## Corrected Claim

RTX 4090 (Ada Lovelace) 的 Tensor Core 仅支持 FP16/BF16/TF32/INT8 硬件矩阵乘法，不支持原生 FP8 (E4M3/E5M2) Tensor Core 运算；FP8 推理必须通过软件路径（dequantize 至 FP16/BF16 后计算，或转为 INT8 后计算），因此 FP8 相比 BF16 的吞吐量增益仅来自显存带宽节省（2x），而非计算单元加速。

## Evidence

先验知识/题面给定，逻辑校验通过：RTX 4090 (Ada Lovelace) 架构确实不支持原生 FP8 Tensor Core 运算（FP8 支持始于 Hopper 架构），其 FP8 推理需通过软件转换，吞吐量增益主要源于显存带宽节省。
