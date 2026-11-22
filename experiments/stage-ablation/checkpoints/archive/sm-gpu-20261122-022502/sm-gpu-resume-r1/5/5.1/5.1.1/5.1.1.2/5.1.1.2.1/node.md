# N845: RTX 5090 的 FP8 Tensor Core 峰值吞吐为 8384 TFLOPS，而 RTX 4090 的 BF16 Tensor Core 峰值吞吐为

- **status**: degraded
- **level**: L5
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 1
- **parent_ids**: N263, N264, N265

## Claim

RTX 5090 的 FP8 Tensor Core 峰值吞吐为 8384 TFLOPS，而 RTX 4090 的 BF16 Tensor Core 峰值吞吐为 330 TFLOPS (无原生 FP8 硬件加速，需软件模拟或降级为 INT8/INT4)。

## Corrected Claim

RTX 5090 的 FP8 Tensor Core 峰值吞吐显著高于 RTX 4090 的 BF16 峰值吞吐，且 RTX 4090 无原生 FP8 硬件加速。

## Evidence

[质询]RTX 5090 的 FP8 峰值吞吐数值（8384 TFLOPS）与官方公布或主流硬件评测数据存在显著偏差（通常约为 3354 TFLOPS 或 6708 TFLOPS 取决于是否计入稀疏性），且 RTX 4090 的 BF16 峰值吞吐（330 TFLOPS）数值偏低（通常约为 1321 TFLOPS 或 2642 TFLOPS 含稀疏性），具体数值可能混淆了稠密/稀疏、不同精度或不同计算单元的定义。 | source=knowledge，逻辑上架构演进符合直觉（5090 > 4090，FP8 > BF16），但具体数值量级与已知硬件规格存在较大出入，且无外部来源支持，故降级。

## Search Query

RTX 5090 FP8 Tensor Core TFLOPS vs RTX 4090 BF16 Tensor Core TFLOPS
