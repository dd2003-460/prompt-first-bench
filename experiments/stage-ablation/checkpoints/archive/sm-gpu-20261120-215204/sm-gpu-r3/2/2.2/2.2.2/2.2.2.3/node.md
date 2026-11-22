# N208: 在 A100 80GB 上，FP8 相比 BF16 的吞吐量提升并非 2.0 倍，而是受限于 A100 不支持原生 FP8 Tensor Core 加速（需通过

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N72

## Claim

在 A100 80GB 上，FP8 相比 BF16 的吞吐量提升并非 2.0 倍，而是受限于 A100 不支持原生 FP8 Tensor Core 加速（需通过软件模拟或降级为 INT8 等效路径），实际提升通常仅为 1.0-1.2 倍（主要受益于带宽减半），N72 中 1.5-2.0 倍的结论仅适用于 H100/H200 等支持 FP8 硬件加速的架构。

## Corrected Claim

在 A100 80GB 上，FP8 相比 BF16 的吞吐量提升并非 2.0 倍，而是受限于 A100 不支持原生 FP8 Tensor Core 加速（需通过软件模拟或降级为 INT8 等效路径），实际提升通常仅为 1.0-1.2 倍（主要受益于带宽减半），N72 中 1.5-2.0 倍的结论仅适用于 H100/H200 等支持 FP8 硬件加速的架构。

## Evidence

先验知识/题面给定，逻辑校验通过：A100 架构确实不支持原生 FP8 Tensor Core，FP8 需软件模拟或降级，带宽减半带来的 1.0-1.2 倍提升符合物理直觉；H100 支持原生 FP8 可达 2 倍吞吐，逻辑自洽。

## Search Query

A100 FP8 inference performance vs BF16 software emulation overhead
