# N486: Dequantization 计算开销量化模型：Overhead_ratio = (Bytes_read_FP4 * Bandwidth_latency + C

- **status**: degraded
- **level**: L5
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N173

## Claim

Dequantization 计算开销量化模型：Overhead_ratio = (Bytes_read_FP4 * Bandwidth_latency + Compute_cycles_dequant) / (Compute_cycles_GEMM_INT8)，在 V100 HBM2 带宽 900GB/s 下，FP4 读取带宽优势被 CPU-GPU 同步或 Kernel Launch 延迟抵消，净收益为负

## Corrected Claim

在 V100 等 GPU 架构中，Dequantization 的计算开销模型通常表示为 Overhead_ratio = (Bytes_read_FP4 * Bandwidth_latency + Compute_cycles_dequant) / (Compute_cycles_GEMM_INT8)。由于 FP4 数据量小带来的带宽节省可能被 CPU-GPU 同步或 Kernel Launch 延迟抵消，因此在特定实现下净收益可能为负，需结合具体系统开销评估。

## Evidence

[质询]该陈述包含具体的硬件参数（V100 HBM2 带宽 900GB/s）和特定的性能结论（净收益为负），属于经验事实。虽然 V100 带宽接近 900GB/s 是合理的，但‘FP4 读取带宽优势被抵消导致净收益为负’这一结论高度依赖于具体的 Kernel 实现、数据布局及同步机制，并非普适的物理或逻辑必然，且缺乏来源支持以证明其在所有或典型场景下成立。 | 经验事实，逻辑自洽但缺来源支持（检索无可用来源）

## Search Query

FP4 dequantization latency vs GEMM compute V100 bandwidth bound
