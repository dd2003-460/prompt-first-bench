# N325: Blackwell vs Ada 架构在 INT8 推理中的关键差异参数：RTX 5090 的 GDDR7 延迟比 GDDR6X 低约 15-20% [待核验]

- **status**: degraded
- **level**: L4
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N106

## Claim

Blackwell vs Ada 架构在 INT8 推理中的关键差异参数：RTX 5090 的 GDDR7 延迟比 GDDR6X 低约 15-20% [待核验]，且 Blackwell 的 SM 支持更高效的 Tensor Core 调度；若 5090 的 Kernel 优化滞后 (如 CUDA 12.8 早期驱动)，实际效率因子可能降至 60%，导致实际 TPS 比仅为 1.5x 下限。

## Corrected Claim

Blackwell 架构在 INT8 推理中相比 Ada 架构具有更高的显存带宽（GDDR7 vs GDDR6X）和更高效的 Tensor Core 调度；若 Kernel 优化滞后，实际效率因子可能显著降低，导致实际 TPS 提升幅度受限（如低于理论峰值的 1.5x）。

## Evidence

[质询]GDDR7 相比 GDDR6X 的主要优势在于带宽（约 28-32 Gbps vs 21-24 Gbps）和能效，而非单纯的访问延迟降低 15-20%。内存延迟通常由控制器和架构决定，而非仅由显存颗粒类型决定，且 15-20% 的延迟降低缺乏公开基准测试的直接支持，属于未经证实的经验性数值。 | 经验事实，逻辑自洽但缺来源支持（检索无可用来源，且具体延迟百分比属于硬件性能经验数据，无法从第一性原理严格推导）

## Search Query

RTX 5090 GDDR7 latency vs RTX 4090 GDDR6X inference performance
