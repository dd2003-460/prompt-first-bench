# N55: INT4 推理的吞吐量提升系数依赖于反量化（Dequantization）开销：在支持 INT4 Tensor Core 的硬件（如 NVIDIA RTX 40

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N9

## Claim

INT4 推理的吞吐量提升系数依赖于反量化（Dequantization）开销：在支持 INT4 Tensor Core 的硬件（如 NVIDIA RTX 4090/3090）上，INT4 相比 BF16 的吞吐量提升约为 2-3 倍；但在缺乏硬件 INT4 加速的 CPU 或老款 GPU 上，软件反量化开销可能导致吞吐量提升低于 1.5 倍甚至接近 1 倍。

## Corrected Claim

INT4 推理的吞吐量提升系数依赖于反量化（Dequantization）开销：在支持 INT4 Tensor Core 的硬件（如 NVIDIA RTX 4090/3090）上，INT4 相比 BF16 的吞吐量提升约为 2-3 倍；但在缺乏硬件 INT4 加速的 CPU 或老款 GPU 上，软件反量化开销可能导致吞吐量提升低于 1.5 倍甚至接近 1 倍。

## Evidence

先验知识/题面给定，逻辑校验通过
