# N337: FP8 回退至 INT8 的性能代价量化：在 RTX 4090 上，INT8 (W8A8) 的 GEMM 吞吐量通常比 FP8 低 15-20%（由于 INT8

- **status**: degraded
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N116

## Claim

FP8 回退至 INT8 的性能代价量化：在 RTX 4090 上，INT8 (W8A8) 的 GEMM 吞吐量通常比 FP8 低 15-20%（由于 INT8 需要额外的 dequantize 操作且 Tensor Core 利用率略低），具体公式为 Throughput_INT8 = Throughput_FP8 * (1 - Delta_Perf)，其中 Delta_Perf ≈ 0.15-0.20 [待核验]，此性能损失需计入 ETPD 分母中的有效吞吐。

## Corrected Claim

在 RTX 4090 上，INT8 (W8A8) 的 GEMM 吞吐量与 FP8 相比可能存在性能差异，具体取决于软件栈优化程度，通常认为两者在 Tensor Core 利用率上接近，但 INT8 可能因 dequantize 开销略低，具体 Delta_Perf 需根据实际基准测试确定，而非固定为 15-20%。

## Evidence

[质询]数值量级存疑：RTX 4090 的 Tensor Core 对 FP8 和 INT8 的峰值吞吐量在理论架构上通常是对等的（均为 2x FP16 或更高，取决于具体指令集支持情况），且 INT8 的 dequantize 开销在现代 GPU 上通常被高度优化，15-20% 的固定性能损失缺乏广泛的基准测试支持，可能混淆了特定软件栈（如 cuBLAS 特定版本）的优化差异与硬件本质差异。 | 先验知识/题面给定，逻辑校验通过，但具体数值（15-20%）属于经验事实且缺乏来源直接支持，存在不确定性。

## Search Query

RTX 4090 INT8 vs FP8 inference throughput benchmark comparison
