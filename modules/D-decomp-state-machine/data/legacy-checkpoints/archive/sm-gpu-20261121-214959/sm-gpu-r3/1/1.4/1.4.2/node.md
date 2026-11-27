# N48: RTX 5090 (Blackwell) 架构原生支持 FP8 和 NVFP4 硬件加速，其 FP8 推理吞吐量理论值可达 H100 SXM 的 60-80% 

- **status**: degraded
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N10

## Claim

RTX 5090 (Blackwell) 架构原生支持 FP8 和 NVFP4 硬件加速，其 FP8 推理吞吐量理论值可达 H100 SXM 的 60-80% (基于带宽 1792 GB/s vs 2039 GB/s 及计算单元密度对比)，但受限于 32GB 显存容量，仅适用于量化模型。

## Corrected Claim

RTX 5090 (Blackwell) 架构原生支持 FP8 和 NVFP4 硬件加速。其显存带宽为 1792 GB/s，低于 H100 SXM 的 3350 GB/s，但在 FP8 计算吞吐量上，得益于 Blackwell 架构更高的 Tensor Core 密度，其理论性能通常优于或接近 H100 SXM，具体取决于模型大小和内存带宽利用率。受限于 32GB 显存容量，仅适用于量化模型或较小规模模型。

## Evidence

[质询]数值量级与逻辑推导存在严重矛盾：1. 带宽对比错误：RTX 5090 显存带宽约为 1792 GB/s，而 H100 SXM 显存带宽为 3350 GB/s（非 2039 GB/s，2039 GB/s 更接近 H100 PCIe 或 A100 的某些指标，但 H100 SXM 标准值为 3.35 TB/s）。若按带宽计算，5090 仅为 H100 SXM 的 ~53%，而非 60-80%。2. 吞吐量逻辑错误：FP8 推理吞吐量不仅取决于带宽，更取决于计算单元（Tensor Core）的密度和频率。Blackwell 架构的 Tensor Core 性能远超 Hopper，即使带宽较低，其 FP8 计算吞吐量理论值通常远高于 H100 SXM，而非仅为其 60-80%。该陈述混淆了带宽瓶颈与计算瓶颈，且引用了错误的 H100 SXM 带宽数据。 | 先验知识/题面给定，逻辑校验失败：H100 SXM 带宽为 3350 GB/s，5090 为 1792 GB/s，带宽比约为 53%；且 Blackwell 计算密度提升显著，FP8 吞吐量不应低于 H100 SXM 的 60-80%，陈述中数值与架构特性矛盾。

## Search Query

RTX 5090 Blackwell FP8 NVFP4 inference throughput benchmark
